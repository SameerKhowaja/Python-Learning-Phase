# Three types of Method
# 1. Class Method
# 2. Instance Method
# 3. Static Method


class Student:
    school = "ABC School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, m1_value):
        self.m1 = m1_value

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def PrintSomething():
        print("This is nice School")


s1 = Student(22, 11, 41)
s2 = Student(14, 31, 21)

print(s1.avg())
print(s2.avg())

# Instance Method is Used
print(s2.get_m1())
s2.set_m1(10)
print(s2.get_m1())

# Class Method is Used
print(Student.info())

# Static Method is Used
Student.PrintSomething()