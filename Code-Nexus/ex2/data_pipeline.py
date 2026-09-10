from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.new_lst: list[str] = []
        self.output_rank = 0
        self.total_processed = 0

    def output(self) -> tuple[int, str]:
        if len(self.new_lst) != 0:
            oldest_data = self.new_lst.pop(0)
            current_rank = self.output_rank
            self.output_rank += 1

            return (current_rank, oldest_data)
        else:
            raise IndexError("the list is Empty")

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        elif isinstance(data, list):
            for i in data:
                if (
                    not isinstance(i, (int, float))
                    and not isinstance(data, bool)
                ):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, (int, float)):
                self.new_lst.append(str(data))
                self.total_processed += 1

            else:
                for i in data:
                    self.new_lst.append(str(i))
                    self.total_processed += 1

        else:
            raise TypeError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for i in data:
                if not isinstance(i, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, str):
                self.new_lst.append(str(data))
                self.total_processed += 1

            else:
                for i in data:
                    self.new_lst.append(str(i))
                    self.total_processed += 1
        else:
            raise TypeError("Improper string data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for ky, val in data.items():
                if not (isinstance(ky, str) and isinstance(val, str)):
                    return False
            return True
        elif isinstance(data, list):
            for i in data:
                if isinstance(i, dict):
                    for ky, val in i.items():
                        if not (isinstance(ky, str) and isinstance(val, str)):
                            return False
                else:
                    return False
            return True

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, dict):
                log_text = ""
                for value in data.values():
                    if log_text == "":
                        log_text = value
                    else:
                        log_text += f": {value}"
                self.new_lst.append(log_text.strip())
                self.total_processed += 1
            else:
                for item in data:
                    log_text = ""
                    for value in item.values():
                        if log_text == "":
                            log_text = value
                        else:
                            log_text += f": {value}"
                    self.new_lst.append(log_text.strip())
                    self.total_processed += 1

        else:
            raise TypeError("Improper log data")


class ExportPlugin(Protocol):
    def process_output(
        self,
        data: list[tuple[int, str]]
                     ) -> None:
        pass


class DataStream():

    def __init__(self) -> None:
        self.lst_prosses: list[DataProcessor] = []

    def register_processor(
        self,
        proc: DataProcessor
                          ) -> None:
        self.lst_prosses.append(proc)

    def process_stream(
        self,
        stream: list[Any]
                    ) -> None:
        for data_item in stream:
            flag = 0
            for item in self.lst_prosses:
                if item.validate(data_item):
                    item.ingest(data_item)
                    flag = 1
                    break

            if flag == 0:
                print("DataStream error Can't process element in stream: "
                      f"{data_item}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if self.lst_prosses:
            for item in self.lst_prosses:
                print(f"{item.__class__.__name__}: "
                      f"total {item.total_processed} items processed, "
                      f"remaining {len(item.new_lst)} on processor")
        else:
            print("No processor found, no data")
        print()

    def output_pipeline(
        self,
        nb: int,
        plugin: ExportPlugin
                        ) -> None:
        for item in self.lst_prosses:
            extra_data = []
            for _ in range(nb):
                if item.new_lst:
                    extra_data.append(item.output())
            try:
                plugin.process_output(extra_data)
            except IndexError as e:
                print(e)


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("\nCSV Output:")
        co = 0
        for i in data:
            co += 1
            if len(data) == co:
                print(f"{i[1]}", end="")
            else:
                print(f"{i[1]},", end="")
        print()


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if data:
            print("{")
            for i in data:
                print(f'  "item_{i[0]}": "{i[1]}",')
            print("}")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    o_datastream = DataStream()
    o_datastream.print_processors_stats()

    stream = ["Hello world", [3.14, -1,
              2.71],
              [{"log_level": "WARNING",
               "log_message": "Telnet access! Use ssh instead"},
              {"log_level": "INFO", "log_message": "User wil is connected"}],
              42,
              ["Hi", "five"]]

    o_numprosses = NumericProcessor()
    o_txtprosses = TextProcessor()
    o_logprosses = LogProcessor()

    print("Registering processors")
    o_datastream.register_processor(o_numprosses)
    o_datastream.register_processor(o_txtprosses)
    o_datastream.register_processor(o_logprosses)

    print("Send the same batch of data on stream")
    o_datastream.process_stream(stream)
    o_datastream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    o_datastream.output_pipeline(3, CSVPlugin())
    o_datastream.print_processors_stats()

    # print("Send 3 processed data from each processor to a json plugin:")
    # o_datastream.output_pipeline(3, JSONPlugin())
    # o_datastream.print_processors_stats()


if __name__ == "__main__":
    main()
