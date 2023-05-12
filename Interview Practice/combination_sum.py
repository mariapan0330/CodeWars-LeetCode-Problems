"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.
"""

# EXAMPLE: [2,3,6,7], target=7, answer=[[2,2,3],[7]]
# PLAN:
# sort the numbers
# starting at the beginning, explore all possible combinations with dfs (stop trying if sum > target)
# to do this, check the same number until the sum > target, in which case continue without marking it as a result

# this one doesn't work
def combination_sum(nums, target):
    nums.sort()
    result = []
    stack = [nums[0]]
    curr_combo = []
    curr_combo_sum = 0
    while stack != []:
        print(stack, ",", curr_combo, ",", curr_combo_sum)
        curr = stack.pop()
        curr_combo.append(curr)
        curr_combo_sum += curr
        if curr_combo_sum == target:
            result.append(curr_combo[:])
        if curr_combo_sum > target:
            continue
        for node in nums[::-1]:
            if curr_combo_sum + node > target:
                continue
            stack.append(node)

    return result


def combination_sum2(nums, target):
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