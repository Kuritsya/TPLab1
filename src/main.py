from CalcRating import CalcRating
from CalcRatingRight import GetStudentScores, RightScores, CalcRatingRight
from DataReaderChild import DataReaderChild
from TextDataReader import TextDataReader
import argparse
import sys

def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path

def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = DataReaderChild()
    students = reader.read(path)
    print("Students: ", students)

    rightStudent = CalcRatingRight(students).GetRightStudent()
    if rightStudent == "":
        print("Таких студентов нет")
    else:
        print("Студент с баллыми выше 90: " + rightStudent)


if __name__ == "__main__":
    main()
