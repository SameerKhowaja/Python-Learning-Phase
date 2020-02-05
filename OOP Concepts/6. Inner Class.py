# Class contains another Class then called Inner class

class Student():
    def __init__(self, name, rollno):
        self.SName = name
        self.Srollno = rollno
        self.lap = self.Laptop("HP", "i5", 8)

    def show(self):
        print(self.SName, self.Srollno)
        self.lap.show()

    class Laptop():
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Sameer", 1001)
s2 = Student("ALi", 1002)

s1.show()
s2.show()