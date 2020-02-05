# init is just like constructor
# self is just like this(Other Languages)

class Computer:

    def __init__(self, cpu, ram):
        self.ComputerCPU = cpu
        self.ComputerRAM = ram

    def config(self):
        print("Config is, ", self.ComputerCPU, self.ComputerRAM, "GB")


comp1 = Computer('i5', 16)
comp2 = Computer('i3', 8)

comp1.config()
comp2.config()

