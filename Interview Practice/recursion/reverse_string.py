# reverse a string using recursion
# STEPS:
# 1. What is the base case
# 2. What is the smallest amount of work each call can do
def reverse_string(s):
#    1: Base case
    if s == '':
        return ''
#    2: Smallest unit = modify a single character in a string 
    return reverse_string(s[1:]) + s[0]

print(reverse_string('automatically'))

# input: hello
# ello + h
# llo + e
# lo + l
# o + l
# "" + o
# o + l + l + e + h