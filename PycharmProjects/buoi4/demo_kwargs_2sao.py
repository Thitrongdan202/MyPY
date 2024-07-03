def test(**kwargs):
    print("Đã gọi tôi", kwargs)
    print("Kiểu", type(kwargs))

    a = kwargs.get('a', 5)
    print('a =', a)




test(a=1, b=3, c=6, d=[3, 6, 9])
test(x=1, y=3)


def giai_pt(**kwargs):
    a = kwargs.get('a')
    b = kwargs.get('b')
    c = kwargs.get('c')

    if c==None:
        print(f"Bac 1: {a}X + {b} = 0")
    else:
        print(f"Bac 2: {a}X^2 + {b}X + {c} = 0")


giai_pt(a=2, b=5)
giai_pt(a=2, b=3, c=1)