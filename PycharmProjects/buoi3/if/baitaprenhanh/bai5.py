from datetime import datetime

# Nhập ngày tháng năm từ bàn phím
date_input = input("Nhập ngày tháng năm (dd/mm/yyyy hoặc dd-mm-yyyy): ")

# Kiểm tra định dạng ngày tháng năm
if '-' in date_input:
    parts = date_input.split('-')
elif '/' in date_input:
    parts = date_input.split('/')
else:
    parts = None

# Kiểm tra tính hợp lệ của các phần
is_valid = True
if parts and len(parts) == 3:
    day, month, year = parts
    if day.isdigit() and month.isdigit() and year.isdigit():
        day = int(day)
        month = int(month)
        year = int(year)

        # Kiểm tra tính hợp lệ của ngày tháng năm
        if month < 1 or month > 12:
            is_valid = False
        elif day < 1 or day > 31:
            is_valid = False
        elif month in [4, 6, 9, 11] and day > 30:
            is_valid = False
        elif month == 2:
            # Kiểm tra năm nhuận
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    is_valid = False
            else:
                if day > 28:
                    is_valid = False
        else:
            try:
                datetime(year, month, day)
            except ValueError:
                is_valid = False
    else:
        is_valid = False
else:
    is_valid = False

# In kết quả
if is_valid:
    print("Ngày tháng năm hợp lệ.")
else:
    print("Ngày tháng năm không hợp lệ.")
