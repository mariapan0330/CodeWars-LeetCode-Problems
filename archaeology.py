"""
You are helping an archaeologist decipher some runes. 
He knows that this ancient society used a Base 10 system, 
and that they never start a number with a leading zero. 
He's figured out most of the digits as well as a few operators, 
but he needs your help to figure out the rest.
The archaeologist will give you a simple math expression, of the form

[number][op][number]=[number]

He has converted all of the runes he knows into digits.
The only operators he knows are addition (+),subtraction(-), 
and multiplication (*), so those are the only ones that will appear.
Each number will be in the range from -1000000 to 1000000, 
and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s.
If there are ?s in an expression, they represent a digit rune 
that the archaeologist doesn't know (never an operator, and never a leading -). 
All of the ?s in an expression will represent the same digit (0-9), 
and it won't be one of the other given digits in the expression. 
No number will begin with a 0 unless the number itself is 0, 
therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented 
by the question mark. If more than one digit works, give the lowest one. 
If no digit works, well, that's bad news for the archaeologist - 
it means that he's got some of his runes wrong. output -1 in that case.

Examples:
Input: "1+1=?"
Output: 2
-----------------
Input: "??*??=302?"
Output: 5
-----------------
Input: "??*1=??"
Output: 2

"""

# Time Complexity: O(n*m) | Space Complexity: O(n)
def decipher(ex):
    ex_split = ex.split('=')
    before_equal_sign, after_equal_sign = ex_split[0], ex_split[1]

    found_nums = []
    found_operators = []
    for i, x in enumerate(ex):
        if x in {'0','1','2','3','4','5','6','7','8','9'} and x not in set(found_nums):
            found_nums.append(x)
        if x in {'+', '-', '*'} and x not in set(found_operators):
            found_operators.append(x)
        if i < len(ex)-1 and ex[i] == "?" and ex[i+1] == "?":
            found_nums.append('0')
    
    main_operator = ''
    if '-' in set(found_operators) and len(found_operators) == 1 and ex[0] != '-':
        bef_split = before_equal_sign.split('-')
        main_operator = '-'
    elif '+' in set(found_operators):
        bef_split = before_equal_sign.split('+')
        main_operator = '+'
    elif '*' in set(found_operators):
        bef_split = before_equal_sign.split('*')
        main_operator = '*'
    
    before_pt1, before_pt2 = bef_split[0], bef_split[1]    
    before_total = 0
    after_total = 1
    for x in range(0,10):
        if str(x) not in set(found_nums):
            pt1 = before_pt1.replace('?', str(x))
            pt2 = before_pt2.replace('?', str(x))
            if main_operator == '+':
                before_total = int(pt1) + int(pt2)
            elif main_operator == '-':
                before_total = int(pt1) - int(pt2)
            elif main_operator == '*':
                before_total = int(pt1) * int(pt2)
            after_total = int(after_equal_sign.replace('?', str(x)))
        if before_total == after_total:
            return x
    return -1

    



inp1 = "1+1=?"
inp2 = "??*??=302?"
inp3 = "??*1=??"
inp4 = "??*-1=??"
inp5 = "-2*?=-6"
inp6 = "?*-2=-6"

print(decipher(inp1))
print(decipher(inp2))
print(decipher(inp3))
print(decipher(inp4))
print(decipher(inp5))
print(decipher(inp6))

    