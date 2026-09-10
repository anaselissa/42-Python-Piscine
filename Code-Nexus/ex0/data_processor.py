from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.new_lst: list[str] = []
        self.output_rank = 0

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
            else:
                for i in data:
                    self.new_lst.append(str(i))
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
            else:
                for i in data:
                    self.new_lst.append(str(i))
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

            else:
                for item in data:
                    log_text = ""
                    for value in item.values():
                        if log_text == "":
                            log_text = value
                        else:
                            log_text += f": {value}"
                    self.new_lst.append(log_text.strip())
        else:
            raise TypeError("Improper log data")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num_obj = NumericProcessor()
    num = 42
    str_t = "Hello"
    print(f"Trying to validate input ’{num}’: {num_obj.validate(num)}")
    print(f"Trying to validate input ’Hello’: {num_obj.validate(str_t)}")
    try:
        print("Test invalid ingestion of string ’foo’"
              "without prior validation:\n")
        num_obj.ingest('foo')
    except TypeError as e:
        print("Got exception:", e)

    num_processor = NumericProcessor()
    num_list: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_list}")
    num_processor.ingest(num_list)
    print("Extracting 3 values...")
    rank1, value1 = num_processor.output()
    print(f"Numeric value {rank1}: {value1}")
    rank2, value2 = num_processor.output()
    print(f"Numeric value {rank2}: {value2}")
    rank3, value3 = num_processor.output()
    print(f"Numeric value {rank3}: {value3}")

    print("\nTesting Text Processor...")
    txtProcessor = TextProcessor()
    print("Trying to validate input ’42’: ", txtProcessor.validate(42))
    txt_list = ["Hello", "Nexus", "World"]
    print(f"Processing data: {txt_list}")
    print("Extracting 1 value...")
    txtProcessor.ingest(txt_list)
    rank_txt, value_txt = txtProcessor.output()
    print(f"Text value {rank_txt} : ", value_txt)

    print("\nTesting Log Processor...")
    o_log_Procesor = LogProcessor()
    print("Trying to validate input ’Hello’: ", o_log_Procesor.validate(str_t))

    log_data_lst = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]
    print("Processing data: ", log_data_lst)
    print("Extracting 2 values...")
    o_log_Procesor.ingest(log_data_lst)
    rank_log, value_log = o_log_Procesor.output()
    print(f"Text value {rank_log} : ", value_log)
    rank_log2, value_log2 = o_log_Procesor.output()
    print(f"Text value {rank_log2} : ", value_log2)


if __name__ == "__main__":
    main()
