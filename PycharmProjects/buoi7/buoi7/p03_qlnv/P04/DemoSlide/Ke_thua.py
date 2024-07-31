class A :
    def __init__(self):
        self.a = a

class B:
    def __init__(self, b):

        #super().__init__(a)
        A.__init__(self.a)
        self.b = b


    def printf(self)
        print("a, b", self.a, self.b)

if __name__ == '__main__':
    b = B(1,2)
    b.printf()