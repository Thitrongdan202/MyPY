import random


def chon_ve_so():
    try:
        ve = sorted(random.sample(range(1, 46), 6))
        return ve
    except Exception as e:
        print("Lỗi khi chọn vé số:", e)
        return []


def mua_n_ve_so(n):
    try:
        ve_so = [chon_ve_so() for _ in range(n)]
        return ve_so
    except Exception as e:
        print("Lỗi khi mua vé số:", e)
        return []


def xo_so():
    try:
        so_trung_thuong = sorted(random.sample(range(1, 46), 6))
        return so_trung_thuong
    except Exception as e:
        print("Lỗi khi xổ số:", e)
        return []


def do_ket_qua(ve, ds_trung_thuong):
    try:
        so_trung = len(set(ve) & set(ds_trung_thuong))
        return so_trung
    except Exception as e:
        print("Lỗi khi dò kết quả:", e)
        return 0


def tinh_tien_thuong(so_trung):
    try:
        tien_thuong = {
            3: 30000,
            4: 300000,
            5: 10000000,
            6: 10000000000
        }
        return tien_thuong.get(so_trung, 0)
    except Exception as e:
        print("Lỗi khi tính tiền thưởng:", e)
        return 0


def thong_ke_ket_qua(ds_ve_so, ds_trung_thuong):
    try:
        ket_qua = list(map(lambda ve: do_ket_qua(ve, ds_trung_thuong), ds_ve_so))
        tong_tien = sum(map(tinh_tien_thuong, ket_qua))
        return ket_qua, tong_tien
    except Exception as e:
        print("Lỗi khi thống kê kết quả:", e)
        return [], 0


if __name__ == '__main__':
    try:
        n = int(input("Nhập số lượng vé muốn mua: "))
        ve_so_nguoi_mua = mua_n_ve_so(n)
        ds_trung_thuong = xo_so()

        print("Dãy số người mua:")
        for ve in ve_so_nguoi_mua:
            print(ve)

        print("Dãy số trúng thưởng:", ds_trung_thuong)

        ket_qua, tong_tien = thong_ke_ket_qua(ve_so_nguoi_mua, ds_trung_thuong)

        print("Kết quả từng vé số:", ket_qua)
        print("Tổng tiền thưởng:", tong_tien)
    except Exception as e:
        print("Lỗi:", e)
