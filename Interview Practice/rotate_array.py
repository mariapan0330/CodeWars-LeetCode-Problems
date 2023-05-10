"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example:
    INPUT: nums = [1,2,3,4,5,6,7], k = 3
    OUTPUT: [5,6,7,1,2,3,4]
    WHY: rotate 1 steps to the right: [7,1,2,3,4,5,6]
         rotate 3 steps to the right: [5,6,7,1,2,3,4]
         rotate 2 steps to the right: [6,7,1,2,3,4,5]


Do not return anything, modify nums in-place instead.
"""

# PLAN: 
# until k is done, pop the last number and add it to the beginning
# or try using list slices? [:-k]

def rotate(nums, k):
    end = 0
    for x in range(0,k):  
        end_num = nums.pop()
        nums.insert(0,end_num)
        # nums = nums[-k:] + nums[:-k]
    return nums



nums = [1,2,3,4,5,6,7]
k = 3
# nums = [1,2]
# k = 3
print(rotate(nums, k))

print("--- TESTS ---")
tests = [3,2,1]
print(id(tests))
# tests2 = [4,5,6]
# print(id(tests2))
tests = [7,6,5]
print(id(tests))

tests1 = [x for x in range(1,500000)]
print(id(tests1))
tests1[:] = [10,11,12]
print(id(tests1))

# tests and tests point to different objects in memory
# but tests1 is reassigned in place with the slice [:], so it points to the same obj in memory
# spent way too long trying to figure out why the tests and tests1 have the same unique ID though
# and it looks like Python can reuse IDs for similar objects, but this is not guaranteed behavior