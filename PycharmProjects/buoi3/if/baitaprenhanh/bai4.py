# Nhập số km quãng đường đi được
km = float(input("Nhập số km quãng đường đi được: "))

# Tính tiền taxi theo số km
if km <= 0:
    print("Số km không hợp lệ.")
else:
    total_cost = 0

    if km <= 1:
        total_cost = 20
    elif km <= 3:
        total_cost = 20 + (km - 1) * 13
    elif km <= 8:
        total_cost = 20 + 2 * 13 + (km - 3) * 12
    else:
        total_cost = 20 + 2 * 13 + 5 * 12 + (km - 8) * 10

    # Kiểm tra nếu tổng tiền hơn 100k thì giảm thêm 8%
    if total_cost > 100:
        total_cost *= 0.92

    print(f"Tổng số tiền cần trả là: {total_cost:.2f}k")
