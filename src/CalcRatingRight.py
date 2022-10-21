from Types import DataType


# Определение окончания поиска нужного студента
def RightScores(scores) -> bool:
    isRightScores = True
    for itemScores in scores:
        if itemScores != 90:
            isRightScores = False
    return isRightScores


# Вычисление результатов ученика
def GetStudentScores(student) -> list:
    items = student[1]
    scores = []
    for item in items:
        scores.append(item[1])
    return scores


# Поиск правильного студента
class CalcRatingRight:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def GetRightStudent(self) -> str:
        rightStudent = ""
        for student in self.data.items():
            scores = GetStudentScores(student)
            if RightScores(scores):
                rightStudent = student[0]
        return rightStudent
