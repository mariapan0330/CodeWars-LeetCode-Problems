"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

EXAMPLE: 
INPUT: nums = [2,3,6,7], target=7 
OUTPUT: [[2,2,3],[7]]
"""

nums = [2,3,6,7,10]

def combination_sum(nums, target):
    """
    PLAN
    - sort the numbers
    - go through each number
        - dfs: nodes = possible numbers, explore the same number til sum is too big
        - stack = current sum and the current sequence.
    """
    nums.sort()
    result = []
    for each in nums:
        stack = [(0, each, [each])] # index, sum, sequence
        while len(stack) > 0:
            idx, curr_sum, curr_seq = stack.pop()
            if curr_sum > target:
                continue
            if curr_sum == target:
                curr_seq.sort()
                if curr_seq not in result:
                    result.append(curr_seq)
            for i in range(idx, len(nums)):
                stack.append((i, curr_sum + nums[i], curr_seq + [nums[i]]))
    return result

print(combination_sum(nums, 7))
print(combination_sum(nums, 10))