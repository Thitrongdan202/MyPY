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
        return "NVVP: " + super().__str__() + " Số ngày: " + str(self.__so_ng)

    def tinh_luong_ht(self):
        pass

class NVBH(NhanVien):
    def __init__(self,ma_nv, **kwargs):
        super().__init__(ma_nv,
                         ho_ten=kwargs.get("ho_ten", "Cập nhật sau"),
                         luong_cb=kwargs.get("luong_cb", 0))

        self.__so_sp = kwargs.get('so_sp, 0')

    def __str__(self):
        return "NVBH: " + str([self._ma_nv, self._ho_ten, self._luong_cb, self.luong_ht, self.__so_sp])

    def tinh_luong_ht(self):
        pass
class CongTy:
    class CongTy:
        def __init__(self, ma_ct, ten_ct):
            self.__ma_ct = ma_ct
            self.__ten_ct = ten_ct
            self.__ds = []



if __name__ == '__main__':
    vp1 = NVVP(123, ho_ten="Nguyễn Văn A", luong_cb=1_000_000, so_ng=20)
    print(vp1)

    bh1 = NVBH(124, ho_ten="Nguyễn Văn H", luong_cb=2_000_000, so_sp=20)
    print(bh1)