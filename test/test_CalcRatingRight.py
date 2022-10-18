import pytest

from CalcRatingRight import CalcRatingRight, GetStudentScores, RightScores
from Types import DataType


class TestMyCalculations:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, str,
                                  list, bool]:
        data: DataType = {
            "Петров Петр Петрович":
                [
                    ("химия", 77),
                    ("литература", 88),
                    ("физика", 99)
                ],

            "Валерьев Валерий Валерьевич":
                [
                    ("обществознание", 90),
                    ("история", 90),
                    ("химия", 90),
                    ("литература", 90)
                ]
        }

        rightStudent: str = "Валерьев Валерий Валерьевич"
        scores: list = [77, 88, 99]
        rightScores: bool = False

        return data, rightStudent, scores, rightScores

    def test_init_MyCalculations(self, input_data: tuple[DataType,
                                                         str,
                                                         list,
                                                         bool]) \
            -> None:
        calcRating = CalcRatingRight(input_data[0])
        assert input_data[0] == calcRating.data

    def test_GetRightStudent(self, input_data: tuple[DataType,
                                                     str,
                                                     list,
                                                     bool]) \
            -> None:
        rightStudent = CalcRatingRight(input_data[0]).GetRightStudent()
        assert input_data[1] == rightStudent

    def test_GetStudentScores(self, input_data: tuple[DataType,
                                                      str,
                                                      list,
                                                      bool]) \
            -> None:
        students = list(input_data[0].items())
        student = students[0]
        scores = GetStudentScores(student)
        assert input_data[2] == scores

    def test_RightScores(self, input_data: tuple[DataType,
                                                 str,
                                                 list,
                                                 bool]) \
            -> None:
        students = list(input_data[0].items())
        student = students[0]
        scores = GetStudentScores(student)
        rightScores = RightScores(scores)
        assert input_data[3] == rightScores