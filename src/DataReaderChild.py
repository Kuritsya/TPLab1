from Types import DataType
from DataReader import DataReader
import yaml

from DataReader import DataReader
from Types import DataType


class DataReaderChild(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            students = yaml.load(file, Loader=yaml.Loader)
            for student in students:
                number, items = list(student.items())[0]
                self.students[number] = []
                for item in items.keys():
                    score = items.get(item)
                    self.students[number].append((item, score))

        return self.students