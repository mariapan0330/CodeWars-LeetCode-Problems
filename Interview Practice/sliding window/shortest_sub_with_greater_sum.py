"""
Given a list of numbers, find the shortest subarray with a sum that's >= x
dynamic sliding window
"""

def shortest_sub_greater_sum(nums, x):
    # PLAN: dynamic sliding window
    # start with l=0,r=1 and expand to the right until you meet the condition
    # then decrease the left until you no longer meet the condition
    # track winner
    # track left pointer & right pointer (they are indexes) and current sum
    highscore = len(nums)
    l,r = 0 , 0
    curr_sum = 0

    # go until sum meets criteria
    while r < len(nums):
        curr_sum += nums[r]
        r += 1

        while l < r and curr_sum >= x:
            curr_sum -= nums[l]
            l += 1

            highscore = min(highscore, r - l+1)
    return highscore
        


    return


nums = [1,2,3,4,5,6]
nums = [1,1,1,1,7]
x = 7
# possible = [1,2,3,4,5,6] and almost any sub of that, [3,4], [4,5] [5,6]
# answer = [5,6]
print(shortest_sub_greater_sum(nums, x))