# Nhập chuỗi từ bàn phím
str_input = input("Nhập chuỗi của bạn: ")

# Tính độ dài chuỗi
length = len(str_input)
print(f"Độ dài của chuỗi: {length}")

# Các ký tự đặc biệt cần đếm
special_characters = "!@#$%^&*()-=+./"

# Biến đếm các ký tự đặc biệt, chữ cái thường, chữ số, chữ cái hoa
special_count = 0
lowercase_count = 0
digit_count = 0
uppercase_count = 0

# Biến để lưu các ký tự đã đếm
special_chars_found = []
lowercase_chars_found = []
digit_chars_found = []
uppercase_chars_found = []

# Duyệt qua từng ký tự trong chuỗi
for char in str_input:
    if char in special_characters:
        special_count += 1
        special_chars_found.append(char)
    elif char.islower():
        lowercase_count += 1
        lowercase_chars_found.append(char)
    elif char.isdigit():
        digit_count += 1
        digit_chars_found.append(char)
    elif char.isupper():
        uppercase_count += 1
        uppercase_chars_found.append(char)

# In kết quả
print(f"Số lượng ký tự đặc biệt: {special_count}")
print(f"Các ký tự đặc biệt: {' '.join(special_chars_found)}")

print(f"Số lượng ký tự chữ thường [a-z]: {lowercase_count}")
print(f"Các ký tự chữ thường: {' '.join(lowercase_chars_found)}")

print(f"Số lượng ký tự chữ số [0-9]: {digit_count}")
print(f"Các ký tự chữ số: {' '.join(digit_chars_found)}")

print(f"Số lượng ký tự chữ hoa [A-Z]: {uppercase_count}")
print(f"Các ký tự chữ hoa: {' '.join(uppercase_chars_found)}")
