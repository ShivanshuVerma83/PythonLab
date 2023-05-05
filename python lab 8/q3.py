# Instance Method Example in Python
class Student:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a + self.b)


s1 = Student(1,3)
print(s1.sum())


# Class Method Example in python

class Student:
    name = 'Shivanshu'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def info(cls):
        return cls.name


print(Student.info())


# Static Method Implementation in python
class Student:
    name = 'Student'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def info():
        return "student class is present"


print(Student.info())
