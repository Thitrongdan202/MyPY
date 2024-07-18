def tinh(x = 1):
    return 2 * x + 3

ds = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
new_ds = [(lambda x:x + tinh(x))(item) for item in ds if item % 2 == 0]

print(new_ds) #[9, 15, 21, 27, 33]

ds = [2, 4, 6, 8, 10]

new_ds = [item - 1 + (lambda a:a * 2)(item) for item in ds if item > 2]

print(new_ds)