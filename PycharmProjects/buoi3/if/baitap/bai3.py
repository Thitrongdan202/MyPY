n = int(input("Nhập giá trị nguyên n: "))

result_dict = {}
for i in range(1, n + 1):
    result_dict[i] = i ** i

print("Dict vừa tạo là:", result_dict)
