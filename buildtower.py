# 6kyu

# Build a pyramid-shaped tower given a positive integer number of floors. 
# A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]

# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

def tower_builder(n_floors):
    res = []
    floor = 1
    for floor in range(1, n_floors + 1):
        spaces = " "*(n_floors-floor)
        res.append(f"{spaces}{'*'*((floor*2)-1)}{spaces}")
        floor += 1
    return res

print(tower_builder(6))
print(tower_builder(2))