# GOAL: Given a number n, find n!, or factorial of that number
# 1 (base case): you have reached 1
# 2 (smallest step): add the current number to the result

def factorialize(num):
    if num == 1:
        return 1
    return num + factorialize(num-1)

print(factorialize(5))