import tkinter as tk
from tkinter import ttk

def tinh_tien():
    # Giá tiền cơ bản cho từng dịch vụ
    gia_sms = 1000
    gia_video_call = 5000
    gia_4g = 2000
    gia_bao_goi_nho = 1500
    gia_phut_goi = 300
    gia_dung_luong_net = 2000

    # Tính tổng tiền dịch vụ
    tong_tien = 0
    if var_sms.get():
        tong_tien += gia_sms
    if var_video_call.get():
        tong_tien += gia_video_call
    if var_4g.get():
        tong_tien += gia_4g
    if var_bao_goi_nho.get():
        tong_tien += gia_bao_goi_nho

    so_phut_goi = int(spin_call_minutes.get())
    dung_luong_net = int(spin_net_usage.get())
    tong_tien += so_phut_goi * gia_phut_goi + dung_luong_net * gia_dung_luong_net

    label_total['text'] = f"{tong_tien} vnd"

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đăng ký dịch vụ")

# Tiêu đề
label_title = tk.Label(root, text="ĐĂNG KÝ DỊCH VỤ", font=("Arial", 16, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Thông tin khách hàng
frame_customer = tk.LabelFrame(root, text="Thông tin khách hàng")
frame_customer.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

label_name = tk.Label(frame_customer, text="Họ và tên")
label_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_name = tk.Entry(frame_customer)
entry_name.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

label_gender = tk.Label(frame_customer, text="Giới tính")
label_gender.grid(row=1, column=0, padx=5, pady=5, sticky="w")
combo_gender = ttk.Combobox(frame_customer, values=["Nam", "Nữ"], state="readonly")
combo_gender.current(0)
combo_gender.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Thông tin dịch vụ
frame_service = tk.LabelFrame(root, text="Thông tin dịch vụ")
frame_service.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

# Dịch vụ chọn
var_sms = tk.BooleanVar()
var_video_call = tk.BooleanVar()
var_4g = tk.BooleanVar()
var_bao_goi_nho = tk.BooleanVar()

check_sms = tk.Checkbutton(frame_service, text="SMS", variable=var_sms)
check_sms.grid(row=0, column=0, padx=5, pady=5, sticky="w")

check_video_call = tk.Checkbutton(frame_service, text="Video call", variable=var_video_call)
check_video_call.grid(row=0, column=1, padx=5, pady=5, sticky="w")

check_4g = tk.Checkbutton(frame_service, text="4G", variable=var_4g)
check_4g.grid(row=0, column=2, padx=5, pady=5, sticky="w")

check_bao_goi_nho = tk.Checkbutton(frame_service, text="Báo gọi nhỡ", variable=var_bao_goi_nho)
check_bao_goi_nho.grid(row=0, column=3, padx=5, pady=5, sticky="w")

# Số phút gọi
label_call_minutes = tk.Label(frame_service, text="Số phút gọi")
label_call_minutes.grid(row=1, column=0, padx=5, pady=5, sticky="w")
spin_call_minutes = tk.Spinbox(frame_service, from_=0, to=1000)
spin_call_minutes.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Dung lượng net
label_net_usage = tk.Label(frame_service, text="Dung lượng net")
label_net_usage.grid(row=1, column=2, padx=5, pady=5, sticky="w")
spin_net_usage = tk.Spinbox(frame_service, from_=0, to=1000)
spin_net_usage.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

# Nút Đăng ký và kết quả
button_register = tk.Button(root, text="Đăng ký", command=tinh_tien)
button_register.grid(row=3, column=0, pady=10, padx=20, sticky="ew")

label_total = tk.Label(root, text="0 vnd")
label_total.grid(row=3, column=1, padx=20, pady=10, sticky="w")

root.mainloop()
