import random


# 1. Khởi tạo các nhân viên
def initNhanVien(ds):
    for i in range(1, 301):
        maNV = i
        hoTen = f"Nhân viên {i}"
        luongCB = random.randint(5_000_000, 10_000_000)
        loai_nv = random.choice(["VP", "BH"])
        if loai_nv == "VP":
            so_ng = random.randint(20, 26)
            nv = {
                'ma_nv': maNV,
                'ho_ten': hoTen,
                'luong_cb': luongCB,
                'so_ng': so_ng,
                'luong_ht': 0,
                'loai_nv': "VP"
            }
        else:
            so_sp = random.randint(50, 150)
            nv = {
                'ma_nv': maNV,
                'ho_ten': hoTen,
                'luong_cb': luongCB,
                'so_sp': so_sp,
                'luong_ht': 0,
                'loai_nv': "BH"
            }
        ds.append(nv)


# 2. Xuất các nhân viên
def printNhanVien(ds):
    for nv in ds:
        print(
            f"Mã NV: {nv['ma_nv']}, Họ tên: {nv['ho_ten']}, Lương cơ bản: {nv['luong_cb']}, Lương hằng tháng: {nv['luong_ht']}")


# 3. Tính lương các nhân viên
def tinh_luong_ht(ds):
    for nv in ds:
        if nv['loai_nv'] == "VP":
            nv['luong_ht'] = nv['luong_cb'] + nv['so_ng'] * 150_000
        elif nv['loai_nv'] == "BH":
            nv['luong_ht'] = nv['luong_cb'] + nv['so_sp'] * 18_000


# 4. Tìm nhân viên theo mã nhân viên
def tim_nv_manv(ds, maNV):
    result = list(filter(lambda nv: nv['ma_nv'] == maNV, ds))
    return result[0] if result else None


# 5. Tìm nhân viên có lương hằng tháng cao nhất
def tim_nv_luong_cao_nhat(ds):
    return max(ds, key=lambda nv: nv['luong_ht'], default=None)


# 6. Tìm nhân viên bán hàng có lương hằng tháng thấp nhất
def tim_nv_bh_luong_thap_nhat(ds):
    bh_nv = list(filter(lambda nv: nv['loai_nv'] == "BH", ds))
    return min(bh_nv, key=lambda nv: nv['luong_ht'], default=None)


# Chương trình chính
if __name__ == '__main__':
    ds = []
    initNhanVien(ds)
    tinh_luong_ht(ds)

    print("Danh sách nhân viên:")
    printNhanVien(ds)

    # Tìm nhân viên theo mã nhân viên
    maNV_tim_kiem = 145
    nv_tim_thay = tim_nv_manv(ds, maNV_tim_kiem)
    if nv_tim_thay:
        print(f"\nNhân viên có mã {maNV_tim_kiem}: {nv_tim_thay}")
    else:
        print(f"\nKhông tìm thấy nhân viên có mã {maNV_tim_kiem}")

    # Tìm nhân viên có lương hằng tháng cao nhất
    nv_luong_cao_nhat = tim_nv_luong_cao_nhat(ds)
    print(f"\nNhân viên có lương hằng tháng cao nhất: {nv_luong_cao_nhat}")

    # Tìm nhân viên bán hàng có lương hằng tháng thấp nhất
    nv_bh_luong_thap_nhat = tim_nv_bh_luong_thap_nhat(ds)
    print(f"\nNhân viên bán hàng có lương hằng tháng thấp nhất: {nv_bh_luong_thap_nhat}")
