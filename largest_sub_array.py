# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
#  and return its sum.

# A subarray is a contiguous part of an array.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
# Input: nums = [1]
# Output: 1
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

def largest_sub_array(nums):
    total = sum(nums)
    while total-nums[0] > total or total-nums[-1] > total:
        print("Assessing:", nums[0], nums[-1])
        # if the first number is greater than the last number, get rid of the last number
        if nums[0] > nums[-1]: 
            total -= nums[-1]
            print('Popping:', nums[-1])
            nums.pop()
        else:
            total -= nums[0]
            print('Popping:', nums[0])
            nums.pop(0)
    return total


def largest_sub_array(nums):
    largest_total = float('-inf')
    curr_total = 0
    for x in nums:
        if x > largest_total:
            largest_total = x
        curr_total += x
    return largest_total


nums = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [5,4,-1,7,8]

print(largest_sub_array(nums))
print(largest_sub_array(nums2))

# print(sum([-2,1,-3,4,-1,2,1,-5,4]))
# print(sum([1,-3,4,-1,2,1,-5,4]))