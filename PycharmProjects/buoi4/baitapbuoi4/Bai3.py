import random

# 1. Viết hàm khởi tạo giá trị tự động cho seqA gồm N phần tử
def khoi_tao_seqA():
    N = random.randint(30, 80)
    seqA = [round(random.uniform(-79, 39), 2) if random.choice([True, False]) else random.randint(-79, 39) for _ in range(N)]
    return seqA

# 2. Viết hàm kiểm tra kiểu dữ liệu từng phần tử
def kiem_tra_kieu_du_lieu(seq):
    kieu_du_lieu = [type(item) for item in seq]
    return kieu_du_lieu

# 3. Viết hàm thống kê số lượng phần tử có trong seqA
def thong_ke_so_luong(seq):
    so_luong = len(seq)
    return so_luong

# 4. Viết hàm sắp xếp dãy seqA thành dãy seqB tăng dần
def sap_xep_seqA(seq):
    seqB = sorted(seq)
    return seqB

# 5. Viết hàm tính trung bình các phần tử trong seqA
def tinh_trung_binh(seq):
    trung_binh = sum(seq) / len(seq)
    return trung_binh

# 6. Viết hàm tính giá trị trung bình giữa hai phần tử nằm giữa trong dãy seqB
def trung_binh_giua(seq):
    N = len(seq)
    if N % 2 == 0:
        giua = (seq[N//2 - 1] + seq[N//2]) / 2
    else:
        giua = seq[N//2]
    return giua

# 7. Viết hàm tính khoảng cách giữa hai giá trị max, min trong dãy seqA hoặc seqB
def khoang_cach_max_min(seq):
    max_val = max(seq)
    min_val = min(seq)
    khoang_cach = max_val - min_val
    return khoang_cach

# 8. Viết hàm so sánh các kết quả của câu 5 và câu 6
def so_sanh_trung_binh(trung_binh_seqA, trung_binh_giua_seqB):
    if trung_binh_seqA > trung_binh_giua_seqB:
        return "Trung bình các phần tử trong seqA lớn hơn"
    elif trung_binh_seqA < trung_binh_giua_seqB:
        return "Trung bình các phần tử trong seqA nhỏ hơn"
    else:
        return "Trung bình các phần tử trong seqA bằng với trung bình giữa hai phần tử nằm giữa trong seqB"

# Chạy chương trình chính
seqA = khoi_tao_seqA()
print("Dãy seqA:", seqA)

kieu_du_lieu_seqA = kiem_tra_kieu_du_lieu(seqA)
print("Kiểu dữ liệu của từng phần tử trong seqA:", kieu_du_lieu_seqA)

so_luong_seqA = thong_ke_so_luong(seqA)
print("Số lượng phần tử trong seqA:", so_luong_seqA)

seqB = sap_xep_seqA(seqA)
print("Dãy seqB (sắp xếp tăng dần từ seqA):", seqB)

trung_binh_seqA = tinh_trung_binh(seqA)
print("Trung bình các phần tử trong seqA:", trung_binh_seqA)

trung_binh_giua_seqB = trung_binh_giua(seqB)
print("Giá trị trung bình giữa hai phần tử nằm giữa trong seqB:", trung_binh_giua_seqB)

khoang_cach_seqA = khoang_cach_max_min(seqA)
print("Khoảng cách giữa giá trị max và min trong seqA:", khoang_cach_seqA)

ket_qua_so_sanh = so_sanh_trung_binh(trung_binh_seqA, trung_binh_giua_seqB)
print("So sánh kết quả của câu 5 và câu 6:", ket_qua_so_sanh)
