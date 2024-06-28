# Giải phương trình bậc nhất ax + b = 0
# Nhập các hệ số a và b từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))


if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Nghiệm của phương trình là: x = {x}")

# Giải phương trình bậc hai ax^2 + bx + c = 0
import math

# Nhập các hệ số a, b và c từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    # Nếu a = 0, phương trình trở thành phương trình bậc nhất
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print(f"Nghiệm của phương trình là: x = {x}")
else:
    # Tính delta
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
