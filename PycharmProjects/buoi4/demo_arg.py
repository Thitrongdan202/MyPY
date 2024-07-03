def test(*args, arg: tuple):
    print("Bạn có gọi tôi", args)
    print("Kiểu dữ liệu", type(args))

test(1, 2, (2,3), arg=(2,3))
