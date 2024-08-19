class NhanVien:
    def __init__(self, manv, ho_ten):
        self.__manv = manv
        self.__ho_ten  = ho_ten

    def get_manv(self):
        return self.__manv

    def get_ho_ten(self):
        return self.__ho_ten

    def set_ho_ten(self, ho_ten):
        self.__ho_ten = ho_ten

    def __str__(self):
        return str([self.__manv, self.__ho_ten])

if__name__ == '__main__':
    nv = NhanVien(manv=123, ho_ten="Nguyễn Văn A")
    print(nv.get_manv()

    nv.set_ho_ten("Nguyễn A")


