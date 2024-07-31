class NhanVien:
    def __init__(self, ma_nv, **kwargs):
        self.ma_nv = ma_nv
        self.ho_ten = kwargs.get('ho_ten', 'Cập nhật tên sau')
        self.luong_cb = kwargs.get('luong_cb', 0)
        self.luong_ht = 0

    def __str__(self):
        return "NV: " + str([self.ma_nv, self.ho_ten,
                             self.luong_cb, self.luong_ht])

    def printf(self):
        print("\n")
        print("\tMã NV  :", self.ma_nv)
        print("\tHọ tên  :", self.ho_tenn)
        print("\tLương CB:", self.luong_cb)


if __name__ == "__main__":
    nv1 = NhanVien(123, ho_ten="Nguyễn Văn A", luong_cb=12000000)
    print(nv1.ho_ten)
