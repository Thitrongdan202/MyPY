#Viết hàm tính cộng trừ nhân chia của hai số đưa vào

def tinh(x: int, y: float,) -> tuple:
    """""# Viết hàm tính cộng trừ nhân chia của hai số đưa vào"""
    tong = x + y
    tru = x - y
    nhan = x * y
    chia = x / y

    return tong, tru, nhan, chia

#kq = tinh(3, 8)
#print ("Tong = ", kq[0], "Chia =", kq[3]) / ít khi sử dụng

tong, hieu, tich, thuong = tinh(3.5, 5)

print("Trừ = ", hieu)

print(tinh.__doc__)