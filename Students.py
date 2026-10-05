import csv 
students = []
with open("Students.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader :
        students.append(row)

while True:    
        print("__________________________________")
        print("")
        print("      Student Grade System")
        print("__________________________________")
        print("")
        print("1. Search by student name.")
        print("2. Search by student code.")
        print("3. Check a grade.")
        print("4. Exit.")

        choice = input("Enter your Choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            found = False

            for student in students:
                if student["name"].lower() == name.lower():
                    found = True
                    grade = int(student["grade"])

                    if grade >= 90:
                        evaluation = "Excellent"
                    elif grade >= 80:
                        evaluation = "Very Good"
                    elif grade >=70:
                        evaluation = "Good"
                    elif grade >=50:
                        evaluation = "Pass"
                    else:
                        evaluation ="Fail"

                    print("________________________________")
                    print("")
                    print("student name:", student["name"])
                    print("Student code:", student["code"])
                    print("Grade:", grade)
                    print("Evaluation:", evaluation)

                    if grade >= 50:
                        print("Result: Passed")
                    else:
                        print("Result: Failled")
                    break
            if not found:
                print("Student not found")

        elif choice == "2":
            code = input("Enter student code: ")
            found = False
            for student in students:
                if student["code"] == code:
                    found = True
                    grade = int(student["grade"])

                    if grade >= 90:
                         evaluation = "Excellent"
                    elif grade >= 80:
                         evaluation = "Very Good"
                    elif grade >=70:
                         evaluation = "Good"
                    elif grade >=50:
                         evaluation = "Pass"
                    else:
                         evaluation ="Fail"
                    
                    print("________________________________")
                    print("")
                    print("student name:", student["name"])
                    print("Student code:", student["code"])
                    print("Grade:", grade)
                    print("Evaluation:", evaluation)
                    
                    if grade >= 50:
                        print("Result: Passed")
                    else:
                        print("Result: Failled")
                    break
            if not found:
                print("Student not found")

        elif choice == "3":
            grade = int(input("Enter Your grade: "))
            if grade >= 90: 
                evaluation = "Excellent" 
            elif grade >= 80: 
                evaluation = "Very Good" 
            elif grade >= 70: 
                evaluation = "Good" 
            elif grade >= 50: 
                evaluation = "Pass" 
            else: 
                evaluation = "Fail"
            print("________________________________")
            print("")
            print("Grade:", grade)
            print("Evaluation:", evaluation)
            if grade >= 50:
                print("Result: Passed")
            else:
                print("Result: Failed")

        elif choice == "4":
            print("Thank you for using Student Grade system")
            break
        else:
            print("Invalid choice, please try again")