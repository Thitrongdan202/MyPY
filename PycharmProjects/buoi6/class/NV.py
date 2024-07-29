class NhanVien:
    so_nv = 0
    def __init__(self, ma_nv, ten_nv, luong_cb, kwargs=None):
        #Chúng ta sẽ khai báo thuộc tính của đối tượng trong đây
        self.ma_nv = ma_nv
        self.ten_nv = kwargs.get('ten_nv', "no_name")
        self.luong_cb = kwargs.get(luong_cb, 0)

    def __str__(self):
        return f"|{self.ma_nv}, {self.ten_nv}, {self.luong_cb}|"

    def printNV(self):
        print("Thông tin nhân viên:")
        print("\t+ Mã nhân viên:", self.ma_nv)
        print("\t+ Họ tên:", self.ten_nv)
        print("\t+ Lương cơ bản:", self.luong_cb)

    @classmethod
    def print_so_nv(cls):
        print("So nv:", cls.so_nv)
        print("Số nv:", NhanVien.so_nv)

    @staticmethod
    def tinh_thue(tien: float):
        return tien * 0.1 + NhanVien.so_nv


if __name__ == '__main__':
    s = "Python"

    nv1 = NhanVien(123, ten_nv="Nguyên Văn A", luong_cb=5_600_000)

    nv2 = NhanVien(124)
    #nv.printNV()
    #nv2.NhanVien(214)

    #print("Số nv:", NhanVien.so_nv)
    #print(nv1.so_nv)
    #print(nv1.so_nv)

    NhanVien.print_so_nv()
    nv1.print_so_nv()
    print("Thuế = ", NhanVien.tinh_thue(10_000_000))
    print("Thuế = ", nv1.tinh_thue(11_000_000))

    a = [1, 2, 7, '6']
    list
