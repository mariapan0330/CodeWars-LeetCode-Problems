# 5!
# using recursion (Oct 20)

def factorial(n):
    # base case: when should i exit the recursive loop
    if n < 2:
        return n
    return n * factorial(n-1)


print(factorial(5))
print(factorial(10))


# fibonacci sequence with recursion
def fibo(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]