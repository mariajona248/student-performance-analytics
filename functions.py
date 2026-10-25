# work out marks and grades

def is_number(text):
    if text == "":
        return False
    for char in text:
        if char < "0" or char > "9":
            return False
    return True


def round_two(value):
    number = int(value * 100 + 0.5)
    return number / 100


def calculate_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total


def calculate_average(total, count):
    avg = total / count
    return avg


def assign_grade(avg, bounds):
    if avg >= bounds[0]:
        return "A+"
    elif avg >= bounds[1]:
        return "A"
    elif avg >= bounds[2]:
        return "B"
    elif avg >= bounds[3]:
        return "C"
    elif avg >= bounds[4]:
        return "D"
    else:
        return "F"


def check_pass_fail(marks, pass_mark=35):
    for mark in marks:
        if mark < pass_mark:
            return False
    return True


class Student:
    def __init__(self, name, marks, bounds):
        self.name = name
        self.__marks = marks
        self.bounds = bounds

    def show_report_card(self):
        total = calculate_total(self.__marks)
        avg = calculate_average(total, len(self.__marks))
        grade = assign_grade(avg, self.bounds)
        print("Name:", self.name)
        print("Total:", total, "| Average:", round_two(avg), "| Grade:", grade)
