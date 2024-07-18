
def init_data(ds: list):
    ds.extend([1, 3, 5])

    a = [1, 3, 5]
    b = a

if __name__  == '__main__':
    dsSV = [2, 4, 6]

    init_data(dsSV)

    print(dsSV)