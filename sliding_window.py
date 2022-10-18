"""
Count the number of continuous subarrays of size 3 which do not have any repeating characters 

"""

def good_substrings(s):
    counter = 0
    for i in range(len(s)):
        if len(set(s[i:i+3])) == 3:
            counter += 1
    return counter

print(good_substrings("xyzzaz"))
print(good_substrings("xyzbaz"))
print(good_substrings("aababcabc"))
print(good_substrings("abcdefghaa"))
