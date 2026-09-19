class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


course = Course("Python Programming")

student1 = Student("Franzen")
student2 = Student("Eloise")

course.add_student(student1)
course.add_student(student2)

print("Course:", course.name)
print("Students:")

for student in course.students:
    print(student.name)
