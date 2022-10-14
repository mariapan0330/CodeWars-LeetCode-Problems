my_dict = {
    1: (1,1),
    2: (2,2),
    3: (3,3)
}

# if (1,1) in my_dict.values():
    # my_dict.pop((2,2))
# print(my_dict)


x = 3
y = 2
solution = eval('{}-(2/3)*{}'.format(y,x))
print(solution)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
abc = 'abc'
print(alphabet[3])
print('===')

for i, let in enumerate(alphabet): 
    print(i, alphabet[i % len(abc)])



mys = {1,2,3}
print(max(mys))

print('===')
mys = 'javascript'
# myd1 = {x:0 for x in mys}
# print(myd1['a']+1)

myd = dict()
for x in mys:
    if x not in myd:
        myd[x] = 1
    else:
        myd[x] += 1

# myd = {x:0 if x not in myd else lambda x: myd[x]+1 for x in mys}
print(myd)
myd.pop('a')
print(myd)

import math
print(eval("math.factorial(3)"))

mys = 'abcd'
lett = mys[-1]
print(mys)
print(lett)

mys = '1+23'
print(eval(mys[:-1]))

mytest = None
print(type(mytest))
if mytest is not None:
    print('not none')
else:
    print('none')

num = 3
mys = f''
mys += "{}{}+2"
mycount = 2
# print(eval(mys.format([f'{num}' for x in range(mycount+1)])))

mys = '?abcda?'
mys = mys.replace('?','8')
print(mys)