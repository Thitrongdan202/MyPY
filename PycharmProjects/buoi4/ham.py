week = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ nhật']

e = enumerate(week, start=100)

ds = [None, -2, -3, [], 4, 0, 6, (), -7, '', 8, {}]

f = filter(bool, ds)


print(list(f))


def tinh(x):
    return x + 3

num1 = [1, 2, 3, 4, 5, 6]
num2 = map(tinh,num1)

print(list(num2))