# Instance method
#     Accessor method :- To only fetch the value of instance variable
#     Mutator method :- To modify the value
# classmethod
# staticmethod

class Student:
    school = 'Telusko'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

#Accessor method
    def get_M1(self):
        return self.m1

#Mutator Method
    def set_M1(self,value):
        self.m1 = value

#to work with class variable need classmethod
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is student class .. in OOPS Module")

s1 = Student(22,122,34)
s2 = Student(23,23,23)

print(s1.avg().__floor__())
print(Student.getSchool())
# s1.info()
Student.info()
