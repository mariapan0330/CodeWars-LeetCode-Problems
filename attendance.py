# You are given a string s representing an attendance record
# for a student where each character signifies whether the student was absent, late, or present on that day. 
# The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.

# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more
# consecutive days.

# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days,
#  so is not eligible for the award.

# Linear time and constant space, O(n)
def attendance(record):
    a_count = 0
    l_count = 0
    for c in record: 
        if c == 'A':
            a_count += 1
            l_count = 0
            if a_count > 1:
                return False
        elif c == 'L':
            l_count += 1
            if l_count >= 3:
                return False
        else:
            l_count = 0
    return True


# Linear time and constant space, O(n) but you have to loop thru twice,
# so technically the previous solution is more optimal.
def attendance(record):
    return False if "LLL" in record or record.count('A') > 1 else True

inp = "PPALLP"
inp2 = "PPALLL" 
inp3 = "PLAPALL" 

print(attendance(inp))
print(attendance(inp2))
print(attendance(inp3))