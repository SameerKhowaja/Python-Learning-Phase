class Student:
    def sum(self, a=None, b=None, c=None):
        s=0
        if a is not None and b is not None and c is not None:
            s = a+b+c
        elif a is not None and b is not None:
            s = a+b
        else:
            s = a

        return s


s1 = Student()
print(s1.sum(39, 29, 12))
print(s1.sum(39, 29))
print(s1.sum(39))
