# Danh sách ban đầu
ds_tinh = [('Tiền Giang', 63), ('Long An', 62), ('Vĩnh Long', 64), ('Bình Dương', 60)]

# Sắp xếp danh sách theo số tăng dần
ds_tinh_sap_xep = sorted(ds_tinh, key=lambda x: x[1])

print("Danh sách sau khi sắp xếp tăng dần theo số:")
print(ds_tinh_sap_xep)
