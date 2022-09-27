# 4kyu 

# Since the weather was good, some students decided to go for a walk 
# in the park after the first lectures of the new academic year. 
# There they saw a squirrel, which climbed a tree in a spiral at a 
# constant angle to the ground. They calculated that in one loop the 
# squirrel climbes h meters (vertical height), the height of the tree 
# is equal to H (v in Ruby), and the length of its circumference equals S.

# These calculations were exhausting, so now the students need your help
#  to figure out how many meters the path length of squirrel climbed when 
# it reached the tree top. The result should be rounded to 4 decimal places.

# Code limit: 52 characters

from math import sqrt

def squirrel(p,h,c):
    res = round((h/p)*sqrt(c**2+p**2), 4)
    return int(str(res)[:-2]) if str(res)[-2:] == '.0' else res


def squirrel(p,h,c):return round(h/p*(c*c+p*p)**.5,4)
squirrel = lambda p,h,c: round(h/p*(c*c+p*p)**.5,4)


print(squirrel(4,16,3))
print(squirrel(8,9,37))
print(squirrel(73,97,167))
