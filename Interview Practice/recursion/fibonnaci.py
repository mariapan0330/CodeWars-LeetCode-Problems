# the dreaded fibonnaci sequence
# GOAL: given a number n, print out the fibonnaci sequence for that many steps
# 1 (base case): you reach the count
# 2 (smallest step): this one plus the last one

# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8

def fib(count, left, right):
    if count == 0:
        return left
    print(left + right)
    return fib(count-1, right, right + left)

fib(10, 1, 1)