from abc import ABC, abstractmethod

class abcNhanVien(ABC):
    @abstractmethod
    def tinh_luong_ht(self):
        pass

class NhanVien(abcNhanVien):
    def __init__(self, ma_nv, **kwargs):
        self._ma_nv = ma_nv
        self._ho_ten = kwargs.get('ho_ten', 'Cập nhật tên sau')
        self._luong_cb = kwargs.get('luong_cb', 0)
        self._luong_ht = 0

    def __str__(self):
        return "NV: " + str([self._ma_nv, self._ho_ten,
                   self._luong_cb, self._luong_ht])

    #def tinh_luong_ht(self):
        pass
class NVVP(NhanVien):
    def __init__(self,ma_nv, **kwargs):
        super().__init__(ma_nv,
                         ho_ten=kwargs.get("ho_ten", "Cập nhật sau"),
                         luong_cb=kwargs.get("luong_cb", 0))

        self.__so_ng = kwargs.get('so_ng, 0')
    def __str__(self):
        return ("NVVP: " + super().__str__() + \
                " Số ngày: " + str(self.__so_ng))

    def tinh_luong_ht(self):
        pass

class NVBH(NhanVien):
    def __init__(self,ma_nv, **kwargs):
        super().__init__(ma_nv,
                         ho_ten=kwargs.get("ho_ten", "Cập nhật sau"),
                         luong_cb=kwargs.get("luong_cb", 0))

        self.__so_sp = kwargs.get('so_sp, 0')

    def __str__(self):
        return "NVBH: " + str([self._ma_nv, self._ho_ten,
                               self._luong_cb, self._luong_ht, self.__so_sp])

    def tinh_luong_ht(self):
        pass

class NVQuanLy:
    def __init__(self, ma_nv, **kwargs):
        super().__init__(ma_nv,
                         ho_ten=kwargs.get("ho_ten", "Cập nhật sau"),
                         luong_cb=kwargs.get("luong_cb", 0))

class CongTy:
    def __init__(self, ma_ct, ten_ct):
        self.__ma_ct = ma_ct
        self.__ten_ct = ten_ct
        self.__ds = []

    # Câu 1: Khởi tạo tự động các nhân viên
    def init_ds_nv(self):
        nv0 = NVBH(122, luong_cb=1_000_000)
        nv1 = NVVP(123, ho_ten="Nguyễn Văn A", luong_cb=9_000_000, so_ng=20)
        nv2 = NVBH(124, ho_ten="Nguyễn Văn B", luong_cb=6_000_000, so_sp=90)
        nv3 = NVVP(125, ho_ten="Nguyễn Văn C", luong_cb=7_000_000, so_ng=23)

        self.__ds.extend([nv1, nv2, nv3, nv0])

    # Câu 2: Xuất các nhân viên trong công ty
    def print_ds_nv(self):
        for nv in self.__ds:
            print(nv)

    # Câu 3: Tính lương hằng tháng của các nhân viên trong công ty
    def tinh_luong_ht(self):
        for nv in self.__ds:
            nv.tinh_luong_ht()

    # Câu 4: Tìm nhân viên theo mã nhân viên
    def tim_nv_manv(self, manv):
        for nv in self.__ds:
            if manv == nv._ma_nv:
                return nv
        return None

    # Câu 5: Cập nhật lương cơ bản theo mã nhân viên
    def cap_nhat_luong_cb(self, manv, luong_cb_moi):
        nv = self.tim_nv_manv(manv)
        if nv:
            nv._luong_cb = luong_cb_moi
            nv.tinh_luong_ht()
            return True
        return False

    # Câu 6: Cập nhật số ngày làm của nhân viên văn phòng theo mã nhân viên
    def cap_nhat_so_ngay_lam(self, manv, so_ngay_moi):
        nv = self.tim_nv_manv(manv)
        if nv and isinstance(nv, NVVP):
            nv._NVVP__so_ng = so_ngay_moi
            nv.tinh_luong_ht()
            return True
        return False

    # Câu 7: Tìm nhân viên có lương hằng tháng cao nhất
    def tim_nv_luong_cao_nhat(self):
        if not self.__ds:
            return None
        return max(self.__ds, key=lambda nv: nv._luong_ht)

    # Câu 8: Tìm nhân viên bán hàng có lương hằng tháng thấp nhất
    def tim_nv_bh_luong_thap_nhat(self):
        nv_bh = [nv for nv in self.__ds if isinstance(nv, NVBH)]
        if not nv_bh:
            return None
        return min(nv_bh, key=lambda nv: nv._luong_ht)


if __name__ == '__main__':
    ct = CongTy(369, "Tesla")

    print("Test: 1. Khởi tạo ds nhân viên")
    ct.init_ds_nv()
    ct.print_ds_nv()

    print("Test: 2. Tính lương từng nhân viên")
    ct.tinh_luong_ht()
    ct.print_ds_nv()

    print("\nTest: 3. In danh sách nhân viên trong công ty:")
    ct.print_ds_nv()

    vp1 = NVVP(123, ho_ten="Nguyễn Văn A", luong_cb=1_000_000, so_ng=20)
    print(vp1)

    bh1 = NVBH(124, ho_ten="Nguyễn Văn H", luong_cb=2_000_000, so_sp=20)
    print(bh1)

    print("\nTest: 4. Tìm nhân viên theo mã nhân viên")
    nv = ct.tim_nv_manv(123)
    print("\tNhân viên: ", nv)
    print("\tNhân viên: ", ct.tim_nv_manv(124))

    if ct.tim_nv_manv(125):
        print("Tìm thấy")
    else:
        print("Không thấy")

    print("\nTest: 5. Cập nhật lương cơ bản theo mã nhân viên")
    if ct.cap_nhat_luong_cb(123, 15_000_000):
        print("Cập nhật lương cơ bản thành công")
    else:
        print("Không tìm thấy nhân viên")

    print("\nTest: 6. Cập nhật số ngày làm của nhân viên văn phòng theo mã nhân viên")
    if ct.cap_nhat_so_ngay_lam(123, 25):
        print("Cập nhật số ngày làm thành công")
    else:
        print("Không tìm thấy nhân viên hoặc nhân viên không phải là NVVP")

    print("\nTest: 7. Tìm nhân viên có lương hằng tháng cao nhất")
    nv_luong_cao_nhat = ct.tim_nv_luong_cao_nhat()
    if nv_luong_cao_nhat:
        print("Nhân viên có lương hằng tháng cao nhất: ", nv_luong_cao_nhat)

    print("\nTest: 8. Tìm nhân viên bán hàng có lương hằng tháng thấp nhất")
    nv_bh_luong_thap_nhat = ct.tim_nv_bh_luong_thap_nhat()
    if nv_bh_luong_thap_nhat:
        print("Nhân viên bán hàng có lương hằng tháng thấp nhất: ", nv_bh_luong_thap_nhat)

    print("Test: Tính trừu tượng")
    NVQuanLy(ma_nv=129, ho_ten="Nguyễn Văn A", luong_cb=9_000_000)