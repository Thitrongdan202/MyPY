
def tinh(x, y):
    return x + y

def ham_pt(a, b, c):
    return a + b + c

if __name__ == '__main__':
    a = tinh(1,2)
    print("1. Tính =", a)

    b = (lambda x, y: x + y + ham_pt(x, x, y))(1,2)
    print("2. Tính =", b)