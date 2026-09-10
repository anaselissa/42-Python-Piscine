from abc import ABC, abstractmethod
from typing import Any


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
        print("== DataStream statistics ==")

        if self.lst_prosses:
            for item in self.lst_prosses:
                print(f"{item.__class__.__name__}: "
                      f"total {item.total_processed} items processed, "
                      f"remaining {len(item.new_lst)} on processor")
        else:
            print("No processor found, no data")
        print()


if __name__ == "__main__":
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
    print("Registering Numeric Processor")
    o_datastream.register_processor(o_numprosses)

    print("\nSend first batch of data on stream:", stream)
    o_datastream.process_stream(stream)

    o_datastream.print_processors_stats()

    print("Registering other data processors")
    o_datastream.register_processor(o_txtprosses)
    o_datastream.register_processor(o_logprosses)

    print("Send the same batch again")
    o_datastream.process_stream(stream)
    o_datastream.print_processors_stats()

    print("Consume some elements from the data processors: "
          "Numeric 3, Text2, Log 1")
    try:
        o_numprosses.output()
        o_numprosses.output()
        o_numprosses.output()

        o_txtprosses.output()
        o_txtprosses.output()

        o_logprosses.output()
    except IndexError as e:
        print(e)

    o_datastream.print_processors_stats()
