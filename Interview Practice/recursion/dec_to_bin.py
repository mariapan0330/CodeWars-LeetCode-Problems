# GOAL: Convert a number n given in decimal to binary
# binary of a number is the remainder of that number divided by 2
#  concatinated with the remainder of that number (rounded up) divided by 2
#  and so on until the last number is 0

# STEPS: 
# 1: base case = the given number is 0 (concat nothing)
# 2: smallest step = return this % 2 concat with remainders of the int of this / 2

# my attempt:
def make_binary(num):
    if num == 0:
        return ''
    return make_binary(int(num / 2)) + str(num % 2)

# after video (https://www.youtube.com/watch?v=IJDJ0kBx2LM at 29:54):
def make_binary(num, result):
    if num == 0:
        return result
    result = str(num % 2) + result
    return make_binary(int(num / 2), result)


print(make_binary(233, '0'))