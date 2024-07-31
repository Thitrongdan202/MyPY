class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c

    def __x(self):
        print("A. Private")

    def _y(self):
        print("B. Protected")

    def z(self):
        print("C. Public")


    def printA(self):
        print(self.__a, self._b, self.c)
        self.__x()
        self._y()
        self.z()

class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def test(self):
        print(self.c, self._b)
        print(self.__a)


if __name__ == '__main__':
    d = A(1, 2, 3)
    #d.printA()

    #d._y()
    #d.z()

    e = B(4, 5, 6)
    e.test()
    e,printA()