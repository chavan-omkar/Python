 # Method overloading is not supported in Python

 # Method Overriding
class A:
    def show(self):
        print("Hi from A")

class B(A):
    # pass
    def show(self):
        print("Hi from B")


a1 = B()
a1.show()