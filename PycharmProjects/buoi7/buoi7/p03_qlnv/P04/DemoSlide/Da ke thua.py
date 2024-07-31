class A:
    def __init__(self):
        self.a = a


class B:
    def __init__(self, b):
        self.b = b

class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = a + b

    def printf(self):
        print(self.a, self.b, self.c, sep="\n")
if __name__ == '__main__':
   c = C(2, 3)
   c.printf()