# Kiểm tra điều kiện để a, b, c là 3 cạnh của một tam giác
# Nhập vào 3 số a, b, c
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("a, b, c là 3 cạnh của một tam giác.")
else:
    print("a, b, c không phải là 3 cạnh của một tam giác.")
# Kiểm tra loại tam giác
# Nhập vào 3 số a, b, c
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện để a, b, c là 3 cạnh của một tam giác
if a + b > c and a + c > b and b + c > a:
    print("a, b, c là 3 cạnh của một tam giác.")

    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c or a == c:
        if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            print("Đây là tam giác vuông cân.")
        else:
            print("Đây là tam giác cân.")
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print("Đây là tam giác vuông.")
    else:
        print("Đây là tam giác thường.")
else:
    print("a, b, c không phải là 3 cạnh của một tam giác.")
