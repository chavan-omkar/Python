# Python doesn't support Abstract class directly but we can use ABC(Abstract Base Classes) module

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("Running from Laptop class")

class Whiteboard:
    def write(self):
        print("Its writing")

class Programmer:
    def work(self,com):
        print("Solving bugs")
        com.process()

# com = Computer()
com1 = Laptop()
prog1 = Programmer()

# com.process()
# com1.process()
prog1.work(com1)