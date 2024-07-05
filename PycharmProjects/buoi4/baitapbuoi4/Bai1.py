import math

# Hàm tính căn bậc n từ một số thực
def can_bac_n(so_thuc, n):
    return so_thuc ** (1/n)

# Hàm tính giá trị bình phương của một số dương
def binh_phuong(so_duong):
    if so_duong > 0:
        return so_duong ** 2
    else:
        return "Số không phải là số dương."

# Hàm kiểm tra một số nhập vào là số chẵn có giá trị âm
def kiem_tra_chan_am(so):
    if so < 0 and so % 2 == 0:
        return True
    else:
        return False

# Hàm kiểm tra một số nhập vào: nếu là số âm có giá trị lẻ thì trả về 1, nếu là số dương có giá trị chẵn thì trả về 1, trường hợp khác trả về 0
def kiem_tra_so(so):
    if so < 0 and so % 2 != 0:
        return 1
    elif so > 0 and so % 2 == 0:
        return 1
    else:
        return 0

# Hàm kiểm tra giá trị nhập vào phải thuộc đoạn [-89, 90], nếu sai bắt nhập lại
def kiem_tra_doan():
    while True:
        so = float(input("Nhập vào một số: "))
        if -89 <= so <= 90:
            return so
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")

# Gọi các hàm và xuất kết quả

# 1. Tính căn bậc n của một số thực
so_thuc = float(input("Nhập vàSo một số thực: "))
n = int(input("Nhập vào số nguyên n: "))
print(f"Căn bậc {n} của {so_thuc} là: {can_bac_n(so_thuc, n)}")

# 2. Tính giá trị bình phương của một số dương
so_duong = float(input("Nhập vào một số dương: "))
print(f"Bình phương của {so_duong} là: {binh_phuong(so_duong)}")

# 3. Kiểm tra một số nhập vào là số chẵn có giá trị âm
so = float(input("Nhập vào một số để kiểm tra chẵn âm: "))
print(f"Số {so} là số chẵn âm: {kiem_tra_chan_am(so)}")

# 4. Kiểm tra một số nhập vào
so = float(input("Nhập vào một số để kiểm tra: "))
print(f"Kết quả kiểm tra số {so} là: {kiem_tra_so(so)}")

# 5. Kiểm tra giá trị nhập vào phải thuộc đoạn [-89, 90]
print(f"Giá trị hợp lệ bạn đã nhập là: {kiem_tra_doan()}")
