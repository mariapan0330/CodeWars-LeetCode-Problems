"""
Given an array and size s, find the maximum sum of a subarray of that size.
"""

def max_sum_continuous_sub(nums, s):
    """ my attempt (doesn't work) """
    # PLAN: sliding static window.
    # for loop starting at nums[s-1] 
    # keep a left pointer, and current i is right pointer
    # keep track of current sum and high score.
    # check if current sum is greater than high score; if so, replace hs
    # on move, subtract the left pointer (and move it up one index) and add the right pointer
    sum_ = nums[:s]
    print(sum_)
    result = sum_[:]
    l = 1
    for i, val in enumerate(nums[s:]):
        sum_ += [val]
        sum_.pop(0)
        l += 1
        if sum_ > result:
            result = sum_[:]
    return result

def max_sum_continuous_sub(nums, s):
    """ My attempt after seeing the theory on https://www.youtube.com/watch?v=MK-NZ4hN7rs"""
    # PLAN: Keep track of current running sum
    # keep track of maximum seen thus far (initialized as -inf)
    # to begin, grow the window the target size, keeping track of running sum as you go
    # to continue, subtract the first number in window and add the next one.
        # check if current running sum is better than the max thus far & swap in if so
    tally = 0
    winner = -float('inf')
    left = 0
    for i, num in enumerate(nums):
        tally += num
        if i >= s-1:
            tally -= nums[left]
            left += 1
        if tally > winner:
            winner = tally
    return winner

def max_sum_continuous_sub(nums, s):
    """ His solution (converted to Python) https://www.youtube.com/watch?v=MK-NZ4hN7rs"""
    # PLAN: Keep track of current running sum
    # keep track of maximum seen thus far (initialized as -inf)
    # to begin, grow the window the target size, keeping track of running sum as you go
    # to continue, subtract the first number in window and add the next one.
        # check if current running sum is better than the max thus far & swap in if so
    tally = 0
    winner = -float('inf')
    for i, num in enumerate(nums):
        tally += num
        if i >= s-1:
            winner = max(winner, tally)
            tally -= nums[i - (s - 1)]
    return winner

nums = [4,2,1,7,8,1,2,8,1,0]
#           ^ ^ ^
# answer = 16
print(max_sum_continuous_sub(nums, 3))