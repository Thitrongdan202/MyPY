# Tạo danh sách các số chẵn từ 2020 đến 3838
even_numbers = []
for num in range(2020, 3839):
    if num % 2 == 0:
        even_numbers.append(num)

# Tạo danh sách các số chia hết cho 9 từ danh sách các số chẵn
divisible_by_9 = []
for num in even_numbers:
    if num % 9 == 0:
        divisible_by_9.append(num)

result_string = ""
for num in divisible_by_9:
    result_string += str(num) + "\t"

print(result_string)
