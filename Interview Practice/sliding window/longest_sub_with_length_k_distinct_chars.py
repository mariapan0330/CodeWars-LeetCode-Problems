"""
Given a string, find the length of longest contiguous string of characters
that contain only k distinct charactrs

This is a "sliding window with auxiliary data structure" problem.

INP: str = ['a','a','a','h','h','i','b','c'], k = 2
OUT: 5
WHY: a,a,a,h,h is the longest substring comprised of only two characters

a a a h h i b c
c b i a a a h h
      ^ ^ ^ ^ ^
"""

def longest_sub_k_distinct(string, k):
    """ My answer before seeing concept """
    # PLAN: dynamic sliding window, with hashmap counting the characters seen 
    # for loop, right pointer is curr i 
    # keep a [left pointer], [high score], [hashmap of chars]
    # begin by extending right side until you meet condition
    # while loop until NO LONGER meet the condition:
        # compare current length and high score
        # remove the left side (also remove from hashmap)
    left = 0
    result = 0
    seen = dict()
    for i, char in enumerate(string):
        if char not in seen:
            seen[char] = 0
        seen[char] += 1
        while len(seen) > k:
            result = max(result, i - left - 1)
            seen[string[left]] -= 1

            # removes characters with val of 0
            seen = {key:val for key, val in seen.items() if val > 0}

    return

inp = ['a','a','a','h','h','i','b','c']
k = 2
print(longest_sub_k_distinct(inp, k))