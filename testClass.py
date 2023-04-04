class A:
    def __init__(self):
        print("Class A")

    def testA(self):
        print("testA")

class B(A):
    def __init__(self):
        #super().__init__()
        print("Class B")      

    def testB(self):
        print("testB")      


bb = B()
bb.testA()      