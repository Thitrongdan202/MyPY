class NhanVienVanPhong:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def tinh_luong_ht(self):
        pass
class NhanVienBanHang:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def tinh_luong_ht(self):
        pass
class CongTy:
    def __init__(self):



        self.dsNV = []


    #Câu 1 : Tạo dữ liệu ds Nhân viên
    def init_data_nv(self):
        bh = NhanVienBanHang()




        self.dsNV.extend(([bh, ]))


    #Câu 2: In ds nhân viên trong công ty
    def print_ds_nv(self):
        pass


    #Câu 3: Tính lương hằng thang của các nhân viên trong công ty
    def tinh_luong_ht(self):
        pass

if __name__ == '__name__':
    print("Test: Câu 1: Tạo ds Nhân viên")
    ct = CongTy()
    ct.init_data_nv()

    print("Test: Cau 2: in ds nhan vien trong cong ty")
    ct.print_ds_nv()

    print("Test: Câu 3: tính lương nhân viên trong công ty")
    ct.tinh_luong_ht()
    ct.print_ds_nv()


    l = ["Python", 6, 3]
    l.append('9')
