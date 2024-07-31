# Lớp cơ sở NhanVien
class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_cb = luong_cb
        self.luong_ht = 0  # Lương hằng tháng

    def __str__(self):
        return f"Mã NV: {self.ma_nv}, Họ tên: {self.ho_ten}, Lương cơ bản: {self.luong_cb}, Lương hằng tháng: {self.luong_ht}"


# Lớp NhanVienVanPhong kế thừa từ NhanVien
class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_ng):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.so_ng = so_ng  # Số ngày làm việc

    # Tính lương hằng tháng
    def tinh_luong_ht(self):
        self.luong_ht = self.luong_cb + self.so_ng * 150_000


# Lớp NhanVienBanHang kế thừa từ NhanVien
class NhanVienBanHang(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_sp):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self.so_sp = so_sp  # Số sản phẩm bán được

    # Tính lương hằng tháng
    def tinh_luong_ht(self):
        self.luong_ht = self.luong_cb + self.so_sp * 18_000


# Lớp CongTy quản lý danh sách nhân viên
class CongTy:
    def __init__(self):
        self.dsNV = []  # Danh sách nhân viên

    # Câu 1: Khởi tạo tự động các nhân viên
    def init_data_nv(self):
        nv1 = NhanVienVanPhong(1, "Nguyễn Văn A", 7_000_000, 22)
        nv2 = NhanVienBanHang(2, "Trần Thị B", 8_000_000, 120)
        self.dsNV.extend([nv1, nv2])

    # Câu 2: Xuất các nhân viên trong công ty
    def print_ds_nv(self):
        for nv in self.dsNV:
            print(nv)

    # Câu 3: Tính lương hằng tháng của các nhân viên trong công ty
    def tinh_luong_ht(self):
        for nv in self.dsNV:
            nv.tinh_luong_ht()

    # Câu 4: Tìm nhân viên theo mã nhân viên
    def tim_nv_manv(self, ma_nv):
        for nv in self.dsNV:
            if nv.ma_nv == ma_nv:
                return nv
        return None

    # Câu 5: Tìm nhân viên có lương hằng tháng cao nhất
    def tim_nv_luong_cao_nhat(self):
        if not self.dsNV:
            return None
        return max(self.dsNV, key=lambda nv: nv.luong_ht)

    # Câu 6: Tìm nhân viên bán hàng có lương hằng tháng thấp nhất
    def tim_nv_bh_luong_thap_nhat(self):
        nv_bh = [nv for nv in self.dsNV if isinstance(nv, NhanVienBanHang)]
        if not nv_bh:
            return None
        return min(nv_bh, key=lambda nv: nv.luong_ht)


if __name__ == '__main__':
    # Tạo đối tượng công ty
    ct = CongTy()

    # Test: Câu 1: Tạo danh sách Nhân viên
    ct.init_data_nv()

    # Test: Câu 3: Tính lương nhân viên trong công ty
    ct.tinh_luong_ht()

    # Test: Câu 2: In danh sách nhân viên trong công ty
    ct.print_ds_nv()

    # Test: Tìm nhân viên theo mã nhân viên
    ma_nv_tim_kiem = 2
    nv_tim_thay = ct.tim_nv_manv(ma_nv_tim_kiem)
    if nv_tim_thay:
        print(f"\nNhân viên có mã {ma_nv_tim_kiem}: {nv_tim_thay}")

    # Test: Tìm nhân viên có lương hằng tháng cao nhất
    nv_luong_cao_nhat = ct.tim_nv_luong_cao_nhat()
    if nv_luong_cao_nhat:
        print(f"\nNhân viên có lương hằng tháng cao nhất: {nv_luong_cao_nhat}")

    # Test: Tìm nhân viên bán hàng có lương hằng tháng thấp nhất
    nv_bh_luong_thap_nhat = ct.tim_nv_bh_luong_thap_nhat()
    if nv_bh_luong_thap_nhat:
        print(f"\nNhân viên bán hàng có lương hằng tháng thấp nhất: {nv_bh_luong_thap_nhat}")
