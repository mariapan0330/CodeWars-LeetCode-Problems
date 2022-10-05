"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order.
 The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

"""

# Overall Time: O(n) | Overall Space: O(n)
def increment_array(arr):
    arr_as_int = eval(f"{''.join([str(x) for x in arr])}+1") # time: O(n) | Space: O(n)
    return [x for x in str(arr_as_int)] # time: O(n) | Space: O(n)


print(increment_array([2,3,4,4]))