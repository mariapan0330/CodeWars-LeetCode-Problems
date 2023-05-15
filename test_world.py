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


class Some_Number:
    def __init__(self, num):
        self.num = num

def change_numbers():
    my_set = {1,2,3}
    add_to_set(my_set)
    print(my_set)

    my_list = [1,2,3]
    add_to_list(my_list)
    print(my_list)
    
    my_num = 1
    add_one(my_num)
    print(my_num)

def add_to_set(my_set):
    return my_set.add(4)

def add_to_list(my_list):
    return my_list.append(4)
    
def add_one(num):
    num += 1
    return num



change_numbers()

my_l = [
    [1,2,3],
    [4,5,6]
]
my_l[0][1] = 'b'

for x in my_l:
    print(x)