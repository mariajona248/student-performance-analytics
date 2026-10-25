 Student Performance Analytics System

1. Project Title

Project: Student Performance Analytics System  
Name: J. Maria Jona  
Register Number: 6113231041076  
Course: Python with AI (EWB Courses)

 2. Objective

This project reads student marks from a CSV file and analyses them using Python, NumPy, and Pandas. It calculates the total, average, grade, and pass or fail result for every student. It also displays class results, subject results, department results, top students, and students with low attendance.

The aim is to convert raw marks into clear and meaningful results that teachers can understand easily without examining the code.

 3. Technologies Used

 Python 3.10 or newer
 NumPy
 Pandas
 CSV file for the dataset
 Visual Studio Code (VS Code)
 Git and GitHub
 GitHub Copilot for coding assistance

 How to Run the Project

1. Install the required libraries:

   `pip install pandas numpy`

2. Run the program from the project folder:

   `python main.py`

3. Press Enter to use the default pass mark of 35 and the default number of top students, which is 10. Alternatively, enter your own values.

4. Dataset Description

The file `students.csv` contains 50 student records. The dataset includes the following columns:

1. Student_ID:Student ID ranging from S001 to S050.
2. Name: Student name.
3. Department: CSE, ECE, IT, MECH, or EEE, with 10 students in each department.
4. Maths: Mathematics marks out of 100.
5. Science: Science marks out of 100.
6. English: English marks out of 100.
7. Computer: Computer marks out of 100.
8. Tamil: Tamil marks out of 100.
9. Attendance: Student attendance percentage.

 5. Implementation

The project is implemented through the following steps:

1. The program asks the user to enter the pass mark. If the user presses Enter, the default pass mark of 35 is used.

2. It reads the `students.csv` file using Pandas and displays the first rows, last rows, dataset information, shape, and statistical summary using `describe()`.

3. It demonstrates data selection using column selection and `iloc`.

4. It uses NumPy arrays to calculate each student's total and average marks row-wise using `axis=1`. It also calculates subject averages, highest marks, and lowest marks column-wise using `axis=0`.

5. It uses functions from `functions.py` to calculate total marks, average marks, grades, and pass or fail results.

6. It adds Total, Average, Grade, and Result columns to the DataFrame.

7. It displays class results, subject results, top students, grade counts, and department averages.

8. It identifies students with attendance below 75% using nested conditional statements.

9. It selects a Student of the Day randomly from the top students using the `random` module and displays a message for the top student's grade using `match-case`.

10. It displays report cards for up to three top students using the `Student` class.

11. It provides a menu using a `while` loop to display all students, show students with an average above 75, or exit the program.

Grading Rules

Grades are assigned based on the student's average marks.

 Average Marks Grade 
 90 and above  A+ 
 80 and above  A 
 70 and above  B 
 60 and above  C 
 50 and above  D 
 Below 50      F 

 Pass or Fail Rules

A student passes only if the marks in every subject are equal to or greater than the specified pass mark. The default pass mark is 35.

If a student scores below the pass mark in any subject, the student fails.

Note: Grades depend on average marks, whereas pass or fail depends on the marks obtained in each subject. Therefore, a student can receive an F grade and still pass if every subject mark is at least 35.

For example, Dev Malhotra has an average of 42.8, receives an F grade, but passes because all subject marks meet the pass mark.

 6. Key Features

Functions Used in functions.py

 `calculate_total(marks)`: Calculates the total marks obtained by a student.
 `calculate_average(total, count)`: Calculates the average marks.
 `assign_grade(avg, bounds)`: Assigns a grade based on the average marks and grade boundaries.
 `check_pass_fail(marks, pass_mark)`: Checks whether all subject marks meet the pass mark.
`Student` class: Uses a private marks attribute and a method to display the student's report card.

Main Features

 Calculates total and average marks for each student.
 Assigns grades based on predefined rules.
 Displays pass and fail counts.
 Calculates the highest, lowest, and class average marks.
Performs subject-wise analysis and identifies the best subject.
Displays a list of top students.
Calculates department-wise averages and identifies the best department.
Identifies students with attendance below 75%.
Selects a Student of the Day randomly from the top students.
Generates student report cards.
Provides a menu to view student data.

Python Concepts Used

 Variables and data types
User input and type casting
Operators
Conditional statements: `if`, `elif`, and `else`
Nested conditional statements
`match-case` statements
`for` and `while` loops
Lists, tuples, and sets
Functions with keyword arguments
Random module
Classes and encapsulation
NumPy arrays
Pandas DataFrames
CSV file handling

7. Output and Screenshots

01_data_preview.png
02_class_and_subject_results.png
03_top_students.png
04_pass_fail_grades.png
05_department_attendance.png
06_report_cards_menu.png


 8. Final Outcome

The Student Performance Analytics System successfully analyses all 50 student records and displays the results in a clear and understandable format.

The key results are:

Total students: 50
Students passed: 42
Students failed: 8
Class average: 74.82
Highest student average: 93.0
Lowest student average: 42.0
Top student: Aarav Sharma from CSE, with an average of 93.0
Best subject: Computer
Best department: CSE, with an average of 87.98
Students with attendance below 75%: 8

 Grade Distribution

 Grade  Number of Students 

 A+  4 
 A  18 
 B  12 
 C  9 
 D  5 
 F  2 

The project demonstrates how Python, functions, loops, conditional statements, NumPy, and Pandas can be combined to analyse student performance and generate meaningful academic reports.

9. Challenges and Learning

Challenges Faced

1. Match-case Error: VS Code displayed the error "Match statements require Python 3.10 or newer" because the laptop was using Python 3.9. I installed Python 3.12 and selected it in VS Code using the Select Interpreter option, which resolved the error.

2. Incorrect Python Path: The `py` command pointed to a Python installation that no longer existed. I resolved this by running the program using the full path to the new `python.exe`.

3. Missing Libraries: The new Python installation did not contain Pandas and NumPy. I installed the required libraries using `pip`.

4. Grade F but Pass: I noticed that a student could receive an F grade but still pass. I understood that grades are based on average marks, while pass or fail depends on the marks obtained in every subject.

5. Unnecessary Files: Temporary files such as `tempCodeRunnerFile.py` and the `__pycache__` folder were created automatically. I removed unnecessary files and added a `.gitignore` file before uploading the project to GitHub.

 What I Learned

How to use functions to avoid repeating code.
How to load CSV files using Pandas, select columns, filter rows, and use `iloc`.
How NumPy performs calculations across rows and columns using the `axis` parameter.
 How to use classes, encapsulation, `match-case`, sets, loops, and the `random` module in a single project.
How to create a GitHub repository and upload a project.
 How to use GitHub Copilot for coding assistance, review the generated code, and make changes to understand and explain the implementation.

 10. GitHub Repository

GitHub Repository Link: