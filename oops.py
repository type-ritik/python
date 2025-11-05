class Dog:
    # Special method intenciated
    def __init__(self, name):
        # self.name is an attribute
        self.name = name
        print(name)
        pass

    def get_name(self):
        return self.name

    def jump(self):
        print("jump")

    # Method
    def bark(self):
        print("bark")


# Instance : Actual dog giving it properties and methods that real dog should have


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


obj1 = Student("Tim", 19, 95)
obj2 = Student("Bill", 19, 75)
obj3 = Student("Kit", 18, 85)

course1 = Course("Programming", 2)
course1.add_student(obj1)
course1.add_student(obj2)
print(course1.get_average_grade())
