class A:
    def a(self, b):
        print("Class A. Phương thức a")


class B:
    def a(self, b):
        print("Class B. Phương thức a")
        super().a()


if __name__ == '__main__':
    b = B()
    b.a()