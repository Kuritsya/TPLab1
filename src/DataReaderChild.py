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
                number, items = list(student.items())[0]  # Номер студента, предмет
                self.students[number] = []
                for item in items.keys():
                    score = items.get(item)  # Поиск результата по предмету
                    self.students[number].append((item, score))

        return self.students

    print("Текст для нового коммита")

