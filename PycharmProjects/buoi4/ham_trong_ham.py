def tinh(x: int, y: float) -> tuple:
    """""# Viết hàm tính cộng trừ nhân chia của hai số đưa vào"""
    tong = x + y
    tru = x - y
    nhan = x * y
    chia = x / y

    def xet(z, t):
        return z > t

    return tong, tru, nhan, chia, xet(x, y)

t, h, ti, th, ss = tinh(8,5)
print("So sánh =", ss)