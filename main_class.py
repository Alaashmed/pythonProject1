from course_class import Course
from student_class import Student

course_list = []
student_list = []


def search_course(course_name, courses):
    exist = 0
    for i in courses:
        if i.course_name in course_name:
            return exist
        return -1


def search_student(student_number, student_list):
    found = 0
    for i in student_list:
        if i.student_number in student_number:
            return found
        return -1


while True:
    print("""choose a process
    1- add a course.
    2- print courses info. 
    3- search a course.
    4- add a student.
    5- print student info.
    6- search a student.
    7- exit.
-----------------------------------------""")
    user_input = int(input("enter here: "))

    if user_input == 1:
        course_name = input("enter course name: ")
        while True:
            course_class = input("enter course class (A, B, C)")
            if course_class not in ["A", "B", "C"]:
                print("please try again :( ")
            else:
                break
        course = Course(course_name, course_class)
        course_list.append(course)
        print("Course created successfully")

    elif user_input == 2:
        print("Course Name\t\t\t Course Class\t\t\t")
        for i in course_list:
            print(i.course_name, "\t\t\t\t", i.course_class)

    elif user_input == 3:
        course_name = input("search by course name")
        course_exist = search_course(course_name, course_list)
        if course_exist == -1:
            print("course is not exist\n")
        else:
            print("course is exist: ")
            print(course_list[course_exist].course_name, course_list[course_exist].course_class, "\n")

    elif user_input == 4:
        student_name = input("enter student name: ")
        student_courses = []
        input_courses = input("enter student courses: ")
        student_courses.append(input_courses)
        while True:
            student_class = input("enter student class(A, B, C)")
            if student_class not in ["A", "B", "C"]:
                print("please try again :( ")
            else:
                break
        student = Student(student_name, student_courses, student_class)
        student_list.append(student)

    elif user_input == 5:
        print("Student Number\t\t\tStudent_Name\t\t\t Student Courses\t\t\t Student Class\t\t\t ")
        for i in student_list:
            print(i.student_number, "\t\t\t\t\t", i.student_name, "\t\t\t\t", i .courses, "\t\t\t\t\t", i.student_class)

    elif user_input == 6:
        student_number = input("search by student number: ")
        student_found = search_student(student_number, student_list)
        if student_found == -1:
            print("student is not found\n")
        else:
            print("student is found: ")
            print("student number is ", student_list[student_found].student_number)
            print("Student name is ", student_list[student_found].student_name, "\n")

    elif user_input == 7:
        exit()

    else:
        print("please enter one of the numbers above :) \n")


print()
