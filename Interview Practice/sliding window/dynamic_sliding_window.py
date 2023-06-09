"""
Given an array and sum k, return the length of the smallest subarray that adds to that sum.
INP: nums=[4,2,2,7,8,1,2,8,1,0], k=8
OUT: 1
"""

def shortest_sub_given_sum(nums, k):
    """ My attempt after seeing the concept (doesn't work!) """
    # PLAN: dynamic sliding window
    # keep track of [high score] and [running sum] and [current length]
    # keep [left] and [right] pointer
    # until you reach the end of the array, do this
        # Keep adding onto the right side (and moving right pointer) until you meet the condition
        # compare the length of the current sub to the high score & swap if better (if size=1 at this point, just return 1)
        # remove and subtract elements from the left side (and move left pointer) until condition is met
        # or size = 1
    
    result = len(nums)
    left, right = 0,0
    tally = nums[0]
    length = 1

    while left < len(nums):
        if tally >= k:
            result = min(length, result)
            while left < right:
                tally -= nums[left]
                left += 1
        
        right += 1
        if right < len(nums):
            tally += nums[right]
    return result

def shortest_sub_given_sum(nums, k):
    """ My answer after reviewing answer """
    # PLAN: dynamic sliding window.
    # still one for loop, where right pointer is the curr i
    # keep a left pointer too
    # keep a current running sum
    # keep minimum window size (high score/result)
    # begin by extending the right side of the window until you meet the condition
    # once you meet the condition, check the length against the current high score
    # decrease the left side until it NO LONGER meets the condition

    left = 0
    tally = 0
    result = len(nums)
    for i, num in enumerate(nums):
        tally += num
        while tally >= k:
            result = min(result, i - (left - 1))
            tally -= nums[left]
            left += 1

    return result


nums=[4,2,2,7,8,1,2,8,1,0]
k=8
print(shortest_sub_given_sum(nums, k))