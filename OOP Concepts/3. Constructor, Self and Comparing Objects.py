# pass is used when nothing perform in class
#class Computer:
    #pass


class Computer:

    def __init__(self):
        self.name = "Sameer"
        self.age = 20

    def UpdateAge(self):
        self.age = 30

    def compare(self, c2_instance):
        # C1 is comparing with Other then C1 become self
        if self.age == c2_instance.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

# Get address of Object in Heap
print(id(c1))

# Update c1 name Way1
c1.name = "Ali"

# Update c1 age Way2
c1.UpdateAge()

print(c1.name, c1.age)
print(c2.name, c2.age)

# Compare two Objects
if c1.compare(c2):
    print("Both are Same Object")
else:
    print("Different Object")
