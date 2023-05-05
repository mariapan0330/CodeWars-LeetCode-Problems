# a logarithm is the number that another number has to be raised to, to reach another number
# like, 2^y = 8
# log base 2 of 8 = y
# log base 2 of 8 = 3
# (in computer science, base is 2)

# log(x) = y
# log(8) = 3
# log(16) = 4
# log(32) = 5
# As x doubles, y increases by only 1
# If x represents the length of input, y represents # of steps it takes to run the algorithm


nums = [x for x in range(0,64)]
print(nums)
while len(nums) > 1:
    nums[:] = nums[:(len(nums)//2)]
    print(nums)

# output: 
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
    32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

[0, 1, 2, 3, 4, 5, 6, 7]

[0, 1, 2, 3]

[0, 1]

[0]
"""
