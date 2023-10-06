# must be in the right order: open, read/write, close
import os
file = open('new.txt', 'w')

file.write('Sunday\n')
file.write('Monday\n')
file.write('Tuesday\n')
file.write('Wednesday\n')
file.write('Thursday\n')
file.write('Friday\n')
file.write('Saturday\n')


file = open('new.txt', 'r')
for x in file.read():
    if x == 'a':
        file = open('new.txt', 'w')
        file.write('b')
        file.close()

file.close()

os.remove('./new.txt')