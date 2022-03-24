
class A :

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working from A")

    def feature2(self):
        print("Festure 2 is working")


class B:

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("Feature 1 working from B")

    def feature4(self):
        print("Festure 4 is working")


class C(A,B):

    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().feature2()


# a1 = B()
# a1.__init__()

c1=C()
c1.feature1()
c1.feat()