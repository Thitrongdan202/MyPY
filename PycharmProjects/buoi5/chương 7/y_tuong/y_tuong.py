
def kiem_tra_an_toan(t):
    assert t > 50, "Nhiệt độ quá cao"


def tinh(a, b):

    nhan = a * b

    try:
        chia = a / b
        chia = 0
    except Exception as e:
        print(e)

    return nhan, chia

if __name__ == '__main__':
    x, y = tinh(5, 2)
    print("nhan =", x)
    print("chia =", y)

    #kiem_tra_an_toan(70)

    print("Đã thực hiện trên")

