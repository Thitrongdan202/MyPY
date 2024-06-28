import re

# Danh sách các tên miền hợp lệ
valid_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com", "aol.com", "zoho.com"]

def is_valid_email(email):
    # Kiểm tra xem có chứa ký tự @ và phần sau @ có trong danh sách tên miền hợp lệ
    if '@' not in email:
        return False

    local_part, domain_part = email.split('@', 1)

    if domain_part not in valid_domains:
        return False

    # Kiểm tra phần trước @ có ít nhất 6 ký tự, không chứa khoảng trắng và ký tự đặc biệt
    if len(local_part) < 6:
        return False

    if re.search(r"[ !#$%&'*+/=?^_`{|}~]", local_part):
        return False

    # Nếu tất cả các điều kiện đều đúng, trả về True
    return True

# Nhập chuỗi từ bàn phím
email_input = input("Nhập e-mail của bạn: ")

# Kiểm tra và in kết quả
if is_valid_email(email_input):
    print("E-mail hợp lệ.")
else:
    print("E-mail không hợp lệ.")
