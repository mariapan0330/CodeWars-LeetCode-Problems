items = [
    ['a','a','a','a','a'],
    ['b','b','b','b','b'],
    ['c','c','c','c','c'],
    ['d','d','d','d','d'],
    ['e','e','e','e','e'],
]

# for row_num, row in enumerate(items):
#     for i, val in enumerate(row):
#         print(row_num, val)


def change_numbers():
    num = 1
    num = add_one(num)
    return num

def add_one(num):
    return num + 1


print(change_numbers())