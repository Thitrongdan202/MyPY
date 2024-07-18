num = [2, 8, 9, 3, 5, 1]

new_num = list(filter(lambda x: x % 2 == 1., num))

print(new_num) #[9, 3, 5, 1]