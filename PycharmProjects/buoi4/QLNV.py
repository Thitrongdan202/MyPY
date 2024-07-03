#1
def initNhanVien(ds):
    vp1= {'ma_nv': 123,
          'ho_ten': "Nguyễn Văn A",
          'luong_cb': 7_000_000,
          'so_ng': 21,
          'luong_ht': 0
    }
    bh1 = {'ma_nv': 123,
           'ho_ten': "Nguyễn Văn A",
           'luong_cb': 8_000_000,
           'so_sp': 98,
           'luong_ht': 0
    }
    #ds = []
    ds.extend([vp1, bh1])


#2




#3 Tính lương nhân viên





if __name__== '__main__':
    ds = []
    initNhanVien(ds)
    printNhanVien(ds)
    tinh_luong_ht(ds)
    tim_nv_manv(ds, 145)

