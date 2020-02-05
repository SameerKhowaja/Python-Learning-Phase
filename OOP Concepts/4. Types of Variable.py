# Instance Variable are in class method
# Class Variable are declare in the class

class Car():
    # Class Variable
    wheels = 4

    def __init__(self):
        # Instance Variable
        self.mil = 10
        self.comp = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8

print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)

# If class variable is changed then it will affect all the instances
Car.wheels = 5

print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
