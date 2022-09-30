my_dict = {
    1: (1,1),
    2: (2,2),
    3: (3,3)
}

if (1,1) in my_dict.values():
    my_dict.pop((2,2))
print(my_dict)


x = 3
y = 2
solution = eval('{}-(2/3)*{}'.format(y,x))
print(solution)