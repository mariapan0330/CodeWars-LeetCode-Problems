# GOAL: Given a word s, find if it is a palindrome (the same backwards or forwards)
# PLAN: 
    # 1. Base case = there are 0-1 letters left
    # 2. Smallest amt of work = continue if first and last letter are the same

# example: KAYAK
# example: KAYAAK
def palindrome_detector(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return palindrome_detector(s[1:-1])
    return False
    

ex1 = 'kayak'
ex2 = 'racecar'
ex3 = 'racecars'
print(palindrome_detector(ex1))
print(palindrome_detector(ex2))
print(palindrome_detector(ex3))