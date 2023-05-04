"""
Given a string s, find the length of the longest substring without repeating characters.
"""

# New Plan:
# keep track of high score
# keep track of current substring that we're checking
# for each char in the string, if char is not already in the substring, add it to the curr_substring
# if the char IS in the substring, it's a duplicate 
#   - check if the length of that substring beats the high score (if so, replace hs)
#   - clear the current substring so you can start again
# if you reach the end of the list, check if the last character is a duplicate (if not, fast track it into the high score)

def longest_substring(s):
    hs = 0
    curr_substring = []

    for i, c in enumerate(s):
        if i == len(s)-1:
            if c not in curr_substring and len(curr_substring)+1 > hs:
                hs = len(curr_substring)+1
            
        if c not in curr_substring:
            curr_substring.append(c)
        else:
            if len(curr_substring) > hs:
                hs = len(curr_substring)
            if curr_substring[-1] != c:
                curr_substring = [curr_substring[-1], c]
            else:
                curr_substring = [c]
                
    print(curr_substring)
    return hs


# print(longest_substring('aabcsa'))
# print(longest_substring('aab'))
# print(longest_substring('dvdf'))
print(longest_substring('anviaj'))