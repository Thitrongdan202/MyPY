import random

# Hàm để tạo ra một vé số ngẫu nhiên
def tao_ve_so():
    return sorted(random.sample(range(1, 46), 6))


# Hàm để so sánh dãy số của người mua và dãy số trúng thưởng
def do_ket_qua(ve_so, ds_trung_thuong):
    return len(set(ve_so) & set(ds_trung_thuong))


# Hàm để tính tiền thưởng dựa trên số lượng số trùng nhau
def tinh_tien_thuong(so_trung):
    tien_thuong = {
        3: 30000,
        4: 300000,
        5: 10000000,
        6: 10000000000
    }
    return tien_thuong.get(so_trung, 0)


# Người mua chọn số vé và tạo vé
def mua_ve_so(so_ve):
    ve_so = [sorted(random.sample(range(1, 46), 6)) for _ in range(so_ve)]
    return ve_so


# Máy xổ số tạo ra dãy số trúng thưởng
def xo_so():
    return sorted(random.sample(range(1, 46), 6))


# Hàm thống kê kết quả người chơi
def thong_ke_ket_qua(ds_ve_so, ds_trung_thuong):
    ket_qua = list(map(lambda ve: do_ket_qua(ve, ds_trung_thuong), ds_ve_so))
    tong_tien = sum(map(tinh_tien_thuong, ket_qua))
    return ket_qua, tong_tien


if __name__ == '__main__':
    so_ve = int(input("Nhập số lượng vé muốn mua: "))
    ve_so_nguoi_mua = mua_ve_so(so_ve)
    ds_trung_thuong = xo_so()

    print("Dãy số người mua:")
    for ve in ve_so_nguoi_mua:
        print(ve)

    print("Dãy số trúng thưởng:", ds_trung_thuong)

    ket_qua, tong_tien = thong_ke_ket_qua(ve_so_nguoi_mua, ds_trung_thuong)

    print("Kết quả từng vé số:", ket_qua)
    print("Tổng tiền thưởng:", tong_tien)
