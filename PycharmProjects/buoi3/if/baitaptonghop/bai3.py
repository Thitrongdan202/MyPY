import re

def is_valid_user_id(user_id):
    # Kiểm tra độ dài của ID user
    if len(user_id) < 6 or len(user_id) > 24:
        return False

    # Kiểm tra xem có chứa các ký tự không hợp lệ hoặc khoảng trắng
    if re.search(r"[!@#$%^&*()\-+=\s]", user_id):
        return False

    return True

def is_valid_password(password):
    # Kiểm tra độ dài của password
    if len(password) < 6 or len(password) > 24:
        return False

    # Kiểm tra có ít nhất 1 chữ cái thường [a-z]
    if not re.search(r"[a-z]", password):
        return False

    # Kiểm tra có ít nhất 1 chữ số [0-9]
    if not re.search(r"[0-9]", password):
        return False

    # Kiểm tra có ít nhất 1 chữ cái hoa [A-Z]
    if not re.search(r"[A-Z]", password):
        return False

    # Kiểm tra có ít nhất 1 ký tự đặc biệt [$ # @]
    if not re.search(r"[$#@]", password):
        return False

    return True

# Nhập ID user và password từ bàn phím
user_id = input("Nhập ID user: ")
password = input("Nhập password: ")

# Kiểm tra và in kết quả
if is_valid_user_id(user_id):
    print("ID user hợp lệ.")
else:
    print("ID user không hợp lệ.")

if is_valid_password(password):
    print("Password hợp lệ.")
else:
    print("Password không hợp lệ.")
