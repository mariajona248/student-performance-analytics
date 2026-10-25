import random
import numpy as np
import pandas as pd
from functions import calculate_total, calculate_average, assign_grade
from functions import check_pass_fail, Student
from functions import is_number, round_two


subjects = ["Maths", "Science", "English", "Computer", "Tamil"]
grade_bounds = (90, 80, 70, 60, 50)

print("===== Student Marks =====")
print("Types:", type(subjects), type(grade_bounds))

# ask for the pass mark
pass_input = input("Type the pass mark (press Enter for 35): ")
while pass_input != "" and not is_number(pass_input):
    pass_input = input("Type a whole number from 0 to 100: ")
if pass_input == "":
    pass_mark = 35
else:
    pass_mark = int(pass_input)
while pass_mark > 100:
    pass_input = input("Pass mark must be 100 or less. Try again: ")
    while pass_input != "" and not is_number(pass_input):
        pass_input = input("Type a whole number from 0 to 100: ")
    if pass_input == "":
        pass_mark = 35
    else:
        pass_mark = int(pass_input)

df = pd.read_csv("students.csv")
print("\n===== CSV preview =====")
print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("\nCSV info:")
df.info()
print("Shape (rows, columns):", df.shape)
print("Type:", type(df))
print("\nNames:")
print(df["Name"].head())
print("\nNames and departments:")
print(df[["Name", "Department"]].head())
print("\nFirst row:")
print(df.iloc[0])
print("\nMarks summary:")
print(df[subjects].describe())

# put the marks in a NumPy array
mark_array = np.array(df[subjects])
row_total = np.sum(mark_array, axis=1)
row_avg = np.mean(mark_array, axis=1)
sub_avg = np.mean(mark_array, axis=0)
sub_high = np.max(mark_array, axis=0)
sub_low = np.min(mark_array, axis=0)

totals = []
averages = []
grades = []
results = []

# go through each student one by one
for i in range(len(df)):
    marks = []
    for subject in subjects:
        marks.append(int(df.iloc[i][subject]))
    total = calculate_total(marks)
    avg = calculate_average(total, len(subjects))
    grade = assign_grade(avg, grade_bounds)
    passed = check_pass_fail(marks, pass_mark=pass_mark)
    totals.append(total)
    averages.append(round_two(avg))
    grades.append(grade)
    if passed:
        results.append("Pass")
    else:
        results.append("Fail")

df["Total"] = totals
df["Average"] = averages
df["Grade"] = grades
df["Result"] = results

print("\n===== Class results =====")
print("Highest average:", round_two(np.max(row_avg)))
print("Lowest average:", round_two(np.min(row_avg)))
print("Class average:", round_two(np.mean(row_avg)))
best_i = np.argmax(row_avg)
print("Top student:", df.iloc[best_i]["Name"])
print("First student's NumPy total:", row_total[0])
print("First student's NumPy average:", round_two(row_avg[0]))
print("Whole number and remainder:", int(np.sum(mark_array[0])) // 5,
      "remainder", int(np.sum(mark_array[0])) % 5)

print("\n===== Subject results =====")
for i in range(len(subjects)):
    print(subjects[i], "- average:", round_two(sub_avg[i]),
          "| highest:", sub_high[i], "| lowest:", sub_low[i])
best_subject_i = np.argmax(sub_avg)
print("Best subject by average:", subjects[best_subject_i])

top_input = input("\nHow many top students? (press Enter for 10): ")
while top_input != "" and not is_number(top_input):
    top_input = input("Type a whole number: ")
if top_input == "":
    top_count = 10
else:
    top_count = int(top_input)
while top_count < 1:
    top_input = input("Type at least 1 (press Enter for 10): ")
    if top_input == "":
        top_count = 10
    elif is_number(top_input):
        top_count = int(top_input)
    else:
        top_count = 0

top_df = df.sort_values("Average", ascending=False).head(top_count)
print("\n===== Top students =====")
print(top_df[["Student_ID", "Name", "Department", "Average", "Grade"]])

passed_count = 0
failed_count = 0
# count passes, fails and grades
print("\n===== Pass, fail and grades =====")
for result in df["Result"]:
    if result == "Pass":
        passed_count = passed_count + 1
    else:
        failed_count = failed_count + 1
print("Passed:", passed_count, "| Failed:", failed_count)
grade_list = ["A+", "A", "B", "C", "D", "F"]
for grade in grade_list:
    grade_count = 0
    for student_grade in df["Grade"]:
        if student_grade == grade:
            grade_count = grade_count + 1
    print(grade, "grade:", grade_count)

print("\n===== Department analysis =====")
dept_avg = df.groupby("Department")["Average"].mean().sort_values(ascending=False)
print(dept_avg)
best_dept = ""
best_avg = -1
departments = set(df["Department"])
for department in departments:
    dept_df = df[df["Department"] == department]
    this_avg = dept_df["Average"].mean()
    if this_avg > best_avg:
        best_avg = this_avg
        best_dept = department
print("Best department:", best_dept)
print("\nUnique departments:", set(df["Department"]))

print("\n===== Attendance below 75% =====")
low_att = df[df["Attendance"] < 75]
if len(low_att) == 0:
    print("No students are below 75% attendance.")
for i in range(len(low_att)):
    student = low_att.iloc[i]
    if student["Attendance"] < 75:
        if student["Result"] == "Pass":
            print(student["Name"], "-", student["Attendance"], "%: Not eligible")
        else:
            print(student["Name"], "-", student["Attendance"],
                  "%: Not eligible and failed a subject")

print("\n===== Student of the day =====")
top_names = []
for i in range(len(top_df)):
    top_names.append(top_df.iloc[i]["Name"])
day_pick = random.choice(top_names)
print(day_pick, "was picked from the top students.")

print("\n===== Top student's grade message =====")
grade = top_df.iloc[0]["Grade"]
match grade:
    case "A+":
        print("Excellent work!")
    case "A":
        print("Great job!")
    case "B":
        print("Good work!")
    case _:
        print("Keep practising!")

print("\n===== Report card demo =====")
report_num = len(top_df)
if report_num > 3:
    report_num = 3
for i in range(report_num):
    top_student = top_df.iloc[i]
    marks = []
    for subject in subjects:
        marks.append(int(top_student[subject]))
    student = Student(top_student["Name"], marks, grade_bounds)
    student.show_report_card()
    print("-----")

print("\n===== Data menu =====")
choice = ""
while choice != "3":
    print("1. Show all 50 students")
    print("2. Show students with an average above 75")
    print("3. Exit")
    choice = input("Type 1, 2 or 3: ")
    if choice == "1":
        print(df)
    elif choice == "2":
        print(df[df["Average"] > 75][
            ["Student_ID", "Name", "Department", "Average", "Grade"]])
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Please type 1, 2 or 3.")
