#4kyu
# https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python

# If n is the numerator and d the denominator of a fraction, 
# that fraction is defined a (reduced) proper fraction if and only if GCD(n,d)==1.

# Now, if you consider a given number d, how many proper fractions can be built using d as a denominator?

# You are to build a function that computes how many proper fractions you can build with a given denominator:

import math
def proper_fractions(n):
    count = 0
    for num in range(1,n):
        if math.gcd(num,n) == 1:
            count += 1
    return count

# just for giggles:
def proper_fractions(n):
    return [x for x in map(lambda num: math.gcd(num, n) == 1, range(1,n))].count(True)


print(proper_fractions(1)) #0
print(proper_fractions(2)) #1
print(proper_fractions(5)) #4
print(proper_fractions(15)) #8
print(proper_fractions(25)) #20
