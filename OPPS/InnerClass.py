
class Student:

    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name , self.rollNo)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Apple'
            self.CPU = 'intel'
            self.ram = '16'

        def show(self):
            print(self.brand , self.CPU , self.ram)

s1 = Student('Omkar',7)
s2 = Student('Navin',18)

s1.show()
lap1 = Student.Laptop()
# print(lap1)