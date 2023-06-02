"""
Given an array, find sum of all subarrays of length k

static size cap 
"""

def subarray_sum(nums, k):
    # PLAN: sliding window. Go through the list once
    #  - subtract the last value and add the next value
    # sub = sum(array[:k])
    curr = sum(nums[:k])
    sums = [curr]
    for i in range(1, len(nums)-k+1):
        curr -= nums[i-1]
        curr += nums[i+k-1]

        sums.append(curr)
    return sums


# [6,9,12,15]
print(subarray_sum([1,2,3,4,5,6], 3))