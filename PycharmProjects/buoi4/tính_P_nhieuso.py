def tinh(*args, ** kwargs):...

tinhToan(1,2,3,4,5) #tổng
tinhToan('tich',1,2,3,4,5) #tích
tinhToan(tinh='tong',1,2,3,4,5)
tinhToan(tinh='tich',1,2,3,4,5)
tinhToan(tinh='2t',1,2,3,4,5)
#mặc định là tính tổng

#2
print(tinh(10, hinh='vuong', tinh='cv'))
tinh(50, hinh='vuong', tinh='dt')
tinh(18, hinh='tron', tinh='cv')
tinh(20, tinh='chu nhat', tinh='dt')
print(tinh(20,30, tinh='chu nhat', tinh='cv_dt'))