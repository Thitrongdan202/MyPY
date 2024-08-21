#Họ tên: Thân Trọng Duy
#MSSV: 22730070 => Làm Đề 3
# Câu 1: Khởi tạo dữ liệu nhân viên của trường
class NhanVien:
    def __init__(self, ma_nv, **kwargs):
        self._ma_nv = ma_nv
        self._so_gio_nc = kwargs.get('so_gio_nc', 0)
        self._dinh_muc = kwargs.get('dinh_muc', 0)
        self._so_gio_day = kwargs.get('so_gio_day', 0)
        self._day_ngoai_gio = kwargs.get('day_ngoai_gio', 0)

    def __str__(self):
        return f"Nhân viên mã số: {self._ma_nv}, Giờ NC: {self._so_gio_nc}, Định mức: {self._dinh_muc}, Giờ dạy: {self._so_gio_day}, Ngoài giờ: {self._day_ngoai_gio}"


class TruongDaiHoc:
    def __init__(self):
        self._danh_sach_nv = []

    def khoi_tao(self):
        nv1 = NhanVien("N201", so_gio_nc=980, dinh_muc=720, so_gio_day=560)
        nv2 = NhanVien("N202", so_gio_nc=1624, dinh_muc=900)
        nv3 = NhanVien("N203", so_gio_nc=450, dinh_muc=850, so_gio_day=580)
        nv4 = NhanVien("G301", so_gio_nc=50, dinh_muc=520, so_gio_day=890, day_ngoai_gio=150)
        nv5 = NhanVien("G302", so_gio_nc=560, dinh_muc=720, so_gio_day=521, day_ngoai_gio=120)
        nv6 = NhanVien("G303", so_gio_nc=180, dinh_muc=650, so_gio_day=790, day_ngoai_gio=220)
        nv7 = NhanVien("C101", so_gio_nc=120, dinh_muc=1820, so_gio_day=1790)
        nv8 = NhanVien("C102", so_gio_nc=50, dinh_muc=1650, so_gio_day=1750)
        nv9 = NhanVien("C103", so_gio_nc=0, dinh_muc=1600, so_gio_day=1680)

        self._danh_sach_nv.extend([nv1, nv2, nv3, nv4, nv5, nv6, nv7, nv8, nv9])
# Câu 2 Thực hiện xét nhiệm vụ từng nhân viên của trường
    def danh_gia_nhiem_vu(self, nv):
        if nv._ma_nv.startswith("G"):  # Xử lý cho Giảng viên
            if nv._so_gio_day >= 0.8 * nv._dinh_muc and nv._so_gio_nc >= 0.2 * nv._dinh_muc:
                if nv._so_gio_day + nv._day_ngoai_gio > 1000:
                    return "Vượt mức"
                return "Hoàn thành"
            else:
                return "Không hoàn thành"
        elif nv._ma_nv.startswith("C"):  # Xử lý cho Chuyên viên
            if nv._so_gio_day < nv._dinh_muc:
                return "Hoàn thành"
            elif nv._so_gio_nc > 0 or nv._so_gio_day > 0:
                return "Vượt mức"
            return "Không hoàn thành"
        elif nv._ma_nv.startswith("N"):  # Xử lý cho Nghiên cứu viên
            if nv._so_gio_nc >= nv._dinh_muc:
                return "Hoàn thành"
            elif nv._so_gio_day > 0:
                return "Vượt mức"
            return "Không hoàn thành"
# Câu 3 tìm nhân viên có nhiệm vụ không hoàn thành
    def nhan_vien_khong_hoan_thanh(self):
        return [nv for nv in self._danh_sach_nv if self.danh_gia_nhiem_vu(nv) == "Không hoàn thành"]
# Câu 4 tìm giảng viên và nghiên cứu viên có số giờ nghiên cứu thấp nhất
    def nhan_vien_gio_nc_thap_nhat(self):
        danh_sach_gv_nc = [nv for nv in self._danh_sach_nv if nv._ma_nv.startswith("G") or nv._ma_nv.startswith("N")]
        return min(danh_sach_gv_nc, key=lambda nv: nv._so_gio_nc)
# Câu 5 tìm giảng viên có tổng số giờ dạy và dạy ngoài giờ lớn nhat
    def giang_vien_gio_day_toi_da(self):
        danh_sach_gv = [nv for nv in self._danh_sach_nv if nv._ma_nv.startswith("G")]
        return max(danh_sach_gv, key=lambda nv: nv._so_gio_day + nv._day_ngoai_gio)
# Câu 6 Thiết kế 1 yêu cầu có áp dụng phương thức tĩnh
    @staticmethod
    def tong_gio_lam_viec(nv):
        return nv._so_gio_nc + nv._so_gio_day + nv._day_ngoai_gio


if __name__ == "__main__":
    truong_dh = TruongDaiHoc()
    truong_dh.khoi_tao()

    # Câu 2: Xét nhiệm vụ từng nhân viên trường
    print("Câu 2: Xét nhiệm vụ của từng nhân viên.")
    for nv in truong_dh._danh_sach_nv:
        print(f"Nhân viên {nv._ma_nv} được đánh giá là: {truong_dh.danh_gia_nhiem_vu(nv)}")

    # Câu 3: Tìm nhân viên có nhiệm vụ không hoàn thành
    print("\nCâu 3: Những nhân viên không hoàn thành nhiệm vụ.")
    danh_sach_khong_hoan_thanh = truong_dh.nhan_vien_khong_hoan_thanh()
    for nv in danh_sach_khong_hoan_thanh:
        print(nv._ma_nv)

    # Câu 4: Tìm giảng viên và nghiên cứu viên có số giờ nghiên cứu thấp nhất
    print("\nCâu 4: Nhân viên có số giờ nghiên cứu thấp nhất.")
    nv_nc_thap_nhat = truong_dh.nhan_vien_gio_nc_thap_nhat()
    print(f"Mã nhân viên: {nv_nc_thap_nhat._ma_nv}")

    # Câu 5: Tìm giảng viên có tổng số giờ dạy và ngoài giờ cao nhất
    print("\nCâu 5: Giảng viên có tổng giờ dạy và ngoài giờ cao nhất.")
    gv_tong_gio_cao_nhat = truong_dh.giang_vien_gio_day_toi_da()
    print(f"Giảng viên: {gv_tong_gio_cao_nhat._ma_nv}")

    # Câu 6: Sử dụng phương thức tĩnh
    print("\nCâu 6: Tính tổng số giờ làm việc của mỗi nhân viên.")
    for nv in truong_dh._danh_sach_nv:
        print(f"Nhân viên {nv._ma_nv} có tổng giờ làm việc là: {TruongDaiHoc.tong_gio_lam_viec(nv)}")



