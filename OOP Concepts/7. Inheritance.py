# There are 3 types i.e. Single lvl, Multi-lvl and Multiple Inheritance

class A1():
    @staticmethod
    def featureA1():
        print("This is Feature 1 of A1")

    @staticmethod
    def featureA2():
        print("This is Feature 2 of A1")


class A2():
    @staticmethod
    def featureA3():
        print("This is Feature 1 of A2")

    @staticmethod
    def featureA4():
        print("This is Feature 2 of A2")


# Single Level
class B(A1):
    @staticmethod
    def feature3():
        print("This is Feature 3")

    @staticmethod
    def feature4():
        print("This is Feature 4")


# Multi Level
class C(B):
    @staticmethod
    def feature5():
        print("This is Feature 5")


# Multiple
class D(A1, A2):
    pass


a1 = A1()
print("A1 functions")
a1.featureA1()
a1.featureA2()
print("\n")

a2 = A2()
print("A2 functions")
a2.featureA3()
a2.featureA4()
print("\n")

b = B()
print("B functions")
b.featureA1()
b.featureA2()
b.feature3()
b.feature4()
print("\n")

c = C()
print("C functions")
c.featureA1()
c.featureA2()
c.feature3()
c.feature4()
c.feature5()
print("\n")

d = D()
print("D functions")
d.featureA1()
d.featureA2()
d.featureA3()
d.featureA4()