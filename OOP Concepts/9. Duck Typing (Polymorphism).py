class PyChram:
    @staticmethod
    def execute():
        print("PyChram IDE can:")
        print("Compile")
        print("Debug")
        print("Run")


class MyEditor:
    @staticmethod
    def execute():
        print("MyEditor IDE can:")
        print("Spell Check")
        print("Error Check")
        print("Compile")
        print("Debug")
        print("Run")


class Laptop:
    def code(self, ide):
        ide.execute()


ide1 = PyChram()
ide2 = MyEditor()

Lap1 = Laptop()

Lap1.code(ide1)
print("\n")
Lap1.code(ide2)
