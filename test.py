students = []
courses = []
marks = []

# Function to input information
def input_info(info_type):
    if info_type == "student":
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (dd/mm/yyyy): ")
        students.append((id, name, dob))
    elif info_type == "course":
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append((id, name))
    elif info_type == "mark":
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        mark = float(input("Enter mark: "))
        marks.append((student_id, course_id, mark))

# Function to list information
def list_info(info_type):
    if info_type == "student":
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}")
    elif info_type == "course":
        for course in courses:
            print(f"ID: {course[0]}, Name: {course[1]}")
    elif info_type == "mark":
        for mark in marks:
            print(f"Student ID: {mark[0]}, Course ID: {mark[1]}, Mark: {mark[2]}")

# Main function to drive the program
def main():
    actions = {"1": ("Input student info", "student"),
               "2": ("Input course info", "course"),
               "3": ("Input marks", "mark"),
               "4": ("List students", "student"),
               "5": ("List courses", "course"),
               "6": ("List marks", "mark")}
    
    while True:
        print("\n".join([f"{k}. {v[0]}" for k, v in actions.items()]))
        print("7. Exit")
        option = input("Select an option: ")
        if option in actions:
            action, info_type = actions[option]
            if "Input" in action:
                input_info(info_type)
            else:
                list_info(info_type)
        elif option == "7":
            break
        else:
            print("Invalid option. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
