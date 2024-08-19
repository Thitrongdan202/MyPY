class NhanVien:
    def __init__(self, manv, ho_ten):
        self.__manv = manv
        self.__ho_ten  = ho_ten

    @property
    def ho_ten(self):
        return self.__ho_ten

    @ho_ten.setter
    def ho_ten(self, ho_ten):
        self.__ho_ten = ho_ten

    def __str__(self):
        return str([self.__manv, self.__ho_ten])

if __name__ == '__main__':
    nv = NhanVien(manv=123, ho_ten="Nguyễn Văn A")

    print(nv.ho_ten)
    nv.ho_ten = "Nguyễn A"

    print(nv)


