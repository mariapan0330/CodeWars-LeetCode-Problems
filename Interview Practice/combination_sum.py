"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.
"""

# EXAMPLE: [2,3,6,7], target=7, answer=[[2,2,3],[7]]
# PLAN:
# sort the numbers
# starting at the beginning, explore all possible combinations (stop trying if sum > target)
# to do this, check the same number recursively until the sum > target, in which case return without marking it as a result

def combination_sum(nums, target):
    
    return


def combination_sum(nums, target):
    nums.sort()
    result = []
    def dfs(curr, idx, curr_sum):
        print(curr, idx)
        if curr_sum > target:
            return
        if curr_sum == target:
            result.append(curr)
            return
        for i in range(idx, len(nums)):
            dfs(curr + [nums[i]], i, curr_sum + nums[i])
    dfs([], 0, 0)
    return result



nums = [2,6,7,3]
target = 7
print(combination_sum(nums, target))