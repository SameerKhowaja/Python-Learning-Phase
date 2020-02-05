class Computer:
    def config(self):
        print("i5, 16GB, 1TB")


# Object of Class Computer
c1 = Computer()
c2 = Computer()

# Type of Class
print(type(c1))

# Way1 to call method
Computer.config(c1)

# Way2 to call method (Use Most)
c1.config()
c2.config()
