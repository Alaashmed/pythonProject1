import random


class Student:
    def __init__(self, student_name, courses, student_class):
        self.student_number = str(random.randint(1000, 10000))
        self.student_name = student_name
        self.courses = courses
        self.student_class = student_class




