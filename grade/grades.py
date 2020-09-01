import math

def percent_to_grade(percent, *, suffix = False, round = False):
    grades = {50: "F", 60: "D", 70: "C", 80: "B", 90: "A"}
    if round is True:
        if percent - math.floor(percent) < 0.5:
            percent = math.floor(percent)
        else:
            percent = math.ceil(percent)
    remainder = percent % 10
    closest_10 = percent - (remainder)
    letter_grade = ''
    if closest_10 < 60:
        letter_grade += grades[50]
    elif percent == 100:
        letter_grade += grades[90]
    else:
        letter_grade += grades[closest_10]
    if suffix is True and percent > 60:
        if percent == 100 or remainder >= 7:
            letter_grade += "+"
        elif remainder < 3:
            letter_grade += "-"
    return letter_grade

def calculate_gpa(grade):
    grade_keys = {"A+": 4.33, "A": 4.00, "A-": 3.67, "B+": 3.33, "B": 3.00, "B-": 2.67, "C+": 2.33, "C": 2.00,
                  "C-": 1.67, "D+": 1.33, "D": 1.00, "D-": 0.67, "F": 0.00}
    result = 0
    divisor = 0

    for arg in grade:
        result += grade_keys[arg]
        divisor += 1
    return result / divisor


