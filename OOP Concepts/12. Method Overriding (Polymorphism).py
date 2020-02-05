class A:
    @staticmethod
    def show():
        print("In Show Class A")


class B(A):
    pass


class C(A):
    @staticmethod
    def show():
        print("In Show Class C")


a = A()
a.show()

b = B()
b.show()

c = C()
c.show()
