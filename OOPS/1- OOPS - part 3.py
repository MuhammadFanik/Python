class ReportCard:
    # Step 1 — Set up the constructor. Initialize self.students as an empty dictionary.
    def __init__(self):
        # Each student will be stored like this: { "Ali": { "grades": [], "average": 0 } }
        self.students = {}
        self.menu()

    # Step 2: Build the menu. Same pattern as before, with these options:
    def menu(self):
        menu_input = int(input("""
        1. Press 1 to Add a student
        2. Press 2 to add grades to a student
        3. Press 3 to view a student's report card
        4. Press 4 to view all the students
        5. Press 5 to exit.
        """))
        if menu_input == 1:
            self.add_student()
        elif menu_input == 2:
            self.add_grades()
        elif menu_input == 3:
            self.view_report()
        elif menu_input == 4:
            self.view_all_students()
        else:
            pass

    # Take a student name as input and add them to self.students with an empty grades list and 0 average.
    # If the student already exists, print "Student already exists"
    # Step 3: Add a student
    def add_student(self):
        student_name = input("Enter student name: ")
        if student_name not in self.students:
            self.students[student_name] = {"grades": [], "average": 0}
            print(f"{student_name} added successfully")
        else:
            print("Student already exists")

        self.menu()

    # Step 4: Add Grades.
    # Take a student name and a grade (number) as input. If the student exists, append the grade to their grades list
    # and recalculate their average. If not, print "Student not found".
    def add_grades(self):
        student_name = input("Enter the student's name: ")
        if student_name in self.students:
            grade = int(input("Enter the grade"))
            self.students[student_name]["grades"].append(grade)
            self.students[student_name]["average"] = round(sum(self.students[student_name]["grades"]) / len(self.students[student_name]["grades"]), 2)
            print("Grade added successfully")
        else:
            print("Student record does not exist")

        self.menu()


    # Step 5: View the report card
    def view_report(self):
        student_name = input("Which student's report card would you like to view?")
        if student_name in self.students:
            print(f"Student: {student_name}")
            print(f"Grades: {self.students[student_name]["grades"]}")
            print(f"Average Score: {self.students[student_name]["average"]}")
        else:
            print("Student record does not exist")


    # Step 6: View all the students
    def view_all_students(self):
        if len(self.students) == 0:
            print("No student record found")
        else:
            for student_name, student_data in self.students.items():
                print(f"Student {student_name}, Data {student_data}")

        self.menu()

stu1 = ReportCard()