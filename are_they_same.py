# 6kyu 

# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b))
# that checks whether the two arrays have the "same" elements, 
# with the same multiplicities (the multiplicity of a member is the number 
# of times it appears). "Same" means, here, that the elements in b are the
# elements in a squared, regardless of the order.

def comp(a1, a2):
    if a1 == None or a2 == None or len(a1) != len(a2):
        return False
    for x in a1:
        if x*x not in set(a2):
            return False
        a2.remove(x*x)
    return True



a1 = [121, 144, 19, 161, 19, 144, 19, 11]
b1 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

a2 = [121, 144, 19, 161, 19, 144, 19, 11]
b2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

a3 = [121, 144, 19, 161, 19, 144, 19, 11]
b3 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

a4 = []
b4 = [1]

print(comp(a1, b1))
print(comp(a2, b2))
print(comp(a3, b3))
print(comp(a4, b4))