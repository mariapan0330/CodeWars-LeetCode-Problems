# writing from list
file = open('test_strings.txt', 'w')

lst = [
    'first line',
    'second line',
    'third line',
    'fourth line',
    ]

for x in lst:
    file.write(x + '\n')

file.close()