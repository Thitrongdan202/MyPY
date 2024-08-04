class NhanVien:
    def __init__(self, ma_nv, **kwargs):
        self.ma_nv = ma_nv
        self.ho_ten = kwargs.get('ho_ten', 'Cập nhật tên sau')
        self.luong_cb = kwargs.get('luong_cb', 0)
        self.luong_ht = 0

    def __str__(self):
        return "NV: " + str([self.ma_nv, self.ho_ten,
                   self.luong_cb, self.luong_ht])

    def tinh_luong_ht(self):
        pass
class NVVP(NhanVien):
    def __init__(self,ma_nv, **kwargs):
        super().__init__(ma_nv,
                         ho_ten=kwargs.get("ho_ten", "Cập nhật sau"),
                         luong_cb=kwargs.get("luong_cb", 0))

        self.so_ng = kwargs.get('so_ng, 0')
    def __str__(self):
        return ("NVVP: " + super().__str__() + \
                " Số ngày: " + str(self.so_ng))

    def tinh_luong_ht(self):
        pass

class NVBH(NhanVien):
    def __init__(self,ma_nv, **kwargs):
        super().__init__(ma_nv,
                         ho_ten=kwargs.get("ho_ten", "Cập nhật sau"),
                         luong_cb=kwargs.get("luong_cb", 0))

        self.so_sp = kwargs.get('so_sp, 0')

    def __str__(self):
        return "NVBH: " + str([self.ma_nv, self.ho_ten, self.luong_cb, self.luong_ht, self.so_sp])

    def tinh_luong_ht(self):
        pass
class CongTy:
    class CongTy:
        def __init__(self, ma_ct, ten_ct):
            self.ma_ct = ma_ct
            self.ten_ct = ten_ct
            self.ds = []



if __name__ == '__main__':
    vp1 = NVVP(123, ho_ten="Nguyễn Văn A", luong_cb=1_000_000, so_ng=20)
    print(vp1)

    bh1 = NVBH(124, ho_ten="Nguyễn Văn H", luong_cb=2_000_000, so_sp=20)
    print(bh1)
