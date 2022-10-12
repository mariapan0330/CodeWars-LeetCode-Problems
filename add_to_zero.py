"""
Given an integer n, return any array containing n unique integers 
such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3], [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]

Example 3:
Input: n = 1
Output: [0]
Constraints:
1 <= n <= 1000

"""

def add_to_0(n):
    result = []
    if n%2 != 0: # if the number is odd, add a 0 to the list.
        result.append(0)
    for x in range(1,n//2+1):
        result.append(x)
        result.append(-x)
    return result

print(add_to_0(5))
print(add_to_0(3))
print(add_to_0(1))
