"""
You are given an array of integers arr, return the length of the longest continuous increasing subarray.
A continuous increasing subarray is defined as 2 or more consecutive indices such that arr[i] < arr[i+1] .
Case 1:
Input: arr = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subarray is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subarray, it is not continuous as elements 5 and 7 are separated by element
4.
Case 2:
Input: arr = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subarray is [2] with length 1. Note that it must be strictly
increasing.

"""

# time: O(n) | Space: O(1)
def continuous(arr1):
    counts = set()
    count = 0
    for x in range(len(arr1)):
        if x == 0:
            continue
        if arr1[x] > arr1[x-1]:
            count += 1
            if x == len(arr1)-1:
                counts.add(count)
        else:
            counts.add(count)
            count = 0
    biggest = max(counts)+1
    return biggest if biggest > 2 else 0

arr = [1,3,5,4,7]
arr2 = [2,2,2,2,2]
arr3 = [1,3,5,6,7]
print(continuous(arr))
print(continuous(arr2))
print(continuous(arr3))