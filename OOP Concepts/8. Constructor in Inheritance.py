class A:
    def __init__(self):
        print("Class A called")

    @staticmethod
    def feature1():
        print("Feature A1")

    @staticmethod
    def feature2():
        print("Feature A2")


class B(A):
    def __init__(self):
        print("Class B called")
        super().__init__()

    @staticmethod
    def feature1():
        print("Feature B1")

    @staticmethod
    def feature3():
        print("Feature B3")


class C:
    def __init__(self):
        print("Class C called")

    @staticmethod
    def feature1():
        print("Feature C1")


class C(A, C):
    def __init__(self):
        print("Class C called")
        super().__init__()


a = A()
b = B()

c = C()
c.feature1()
