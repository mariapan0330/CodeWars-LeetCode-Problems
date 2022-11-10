"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
Follow up: Can you solve it in O(n) time and O(1) space?

"""

def are_equal(phrase1, phrase2):
    p1 = eval_phrase(phrase1)
    p2 = eval_phrase(phrase2)
    return p1 == p2


def eval_phrase(phrase):
    result = ''
    for c in phrase:
        if c == "#":
            result = result[:-1]
            continue
        result += c
    return result





s1,t1 = "ab#c", "ad#c"
# true, "ac"

s2,t2 = "ab##", "c#d#"
# true, ""

s3,t3 = "a#c", "b"
# false, c & b

print(are_equal(s1,t1))
print(are_equal(s2,t2))
print(are_equal(s3,t3))