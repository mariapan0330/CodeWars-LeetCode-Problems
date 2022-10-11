"""
5 kyu

Complete the function scramble(str1, str2) that returns true if a portion of
 str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

"""


def scramble(s1,s2):
    checked = 0
    dict1 = dict()
    for x in s1:
        if x not in dict1:
            dict1[x] = 1
        else:
            dict1[x] += 1
    for x in s2:
        if x in dict1 and dict1[x] > 0:
            checked+=1
            dict1[x] -= 1
    return checked == len(s2)


# print(scramble('rkqodlw', 'world'))
# print(scramble('cedewaraaossoqqyt', 'codewars'))
# print(scramble('katas', 'steak'))
# print(scramble('hfchtwkotniug', 'owwin'))
# print(scramble('javascript', 'scriptjava'))
# print(scramble('scriptingjava', 'javascript'))
print(scramble('qltljvsmgmmkhrfi', 'rqmslgqvmjm'))
#               ^  ^  ^^^    ^



