class NhanVien:
    def __init__(self, ma_nv, **kwargs):
        self._ma_nv = ma_nv
        self._ho_ten = kwargs.get('ho_ten', 'Cập nhật tên sau')
        self._luong_cb = kwargs.get('luong_cb', 0)
        self._luong_ht = 0

    def __str__(self):
        return "NV: " + str([self._ma_nv, self._ho_ten,
                   self._luong_cb, self._luong_ht])

    def tinh_luong_ht(self):
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
class CongTy:
        def __init__(self, ma_ct, ten_ct):
            self.__ma_ct = ma_ct
            self.__ten_ct = ten_ct
            self.__ds = []

        # Câu 1: Khởi tạo tự động các nhân viên
        def init_ds_nv(self):
            nv0 = NVBH(122, luong_cb=1_000_000)
            nv1 = NVVP(123, ho_ten="Nguyễn Văn A", luong_cb=9_000_000, so_ng=20)
            nv2 = NVBH(124, ho_ten="Nguyễn Văn B", luong_cb=6_000_000, so_ng=90)
            nv3 = NVVP(125, ho_ten="Nguyễn Văn C", luong_cb=7_000_000, so_ng=23)

            self.__ds.extend([nv1, nv2, nv3, nv0])

        # Câu 2: Xuất các nhân viên trong công ty
        def tinh_luong_ht(self):
            for nv in self.__ds:
                nv.tinh_luong_ht()

        # Câu 3: Tính lương hằng tháng của các nhân viên trong công ty
        def print_ds_nv(self):
            for nv in self.__ds:
                print(nv)

        # Câu 4: Tìm nhân viên theo mã nhân viên
        def tim_nv_manv(self, manv):
            for nv in self.__ds:
                if manv == nv._ma_nv:
                    return nv

if __name__ == '__main__':
    ct = CongTy(369, "Tesla")

    print("Test: 1. Khởi tạo ds nhân viên")
    ct.init_ds_nv()
    ct.print_ds_nv()

    print("Test: 2.Tính lương từng nhân viên")
    ct.tinh_luong_ht()

    print("\nTest: 3. In danh sách nhân viên trong công ty:")
    ct.print_ds_nv()

    vp1 = NVVP(123, ho_ten="Nguyễn Văn A", luong_cb=1_000_000, so_ng=20)
    print(vp1)

    bh1 = NVBH(124, ho_ten="Nguyễn Văn H", luong_cb=2_000_000, so_sp=20)
    print(bh1)

    print("\nTest: 4.Tìm nhân viên theo mã nhân viên")
    nv = ct.tim_nv_manv(123)
    print("\t Nhan viên: ", nv)
    print("\t Nhan viên: ", ct.tim_nv_manv(124))

    if ct.tim_nv_manv(125):
        print("Tìm thấy")
    else:
        print("Không thấy")
