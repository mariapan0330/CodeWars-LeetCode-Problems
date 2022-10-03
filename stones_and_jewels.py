"""
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type 
of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

"""
def stones_and_jewels(jewels,stones):
    jewels = set(jewels)
    count = 0
    for stone in stones:
        count += 1 if stone in jewels else 0
    return count

jewels1 = "aA"
stones1 = "aAAbbbb"
jewels2 = "z"
stones2 = "ZZ"

print(stones_and_jewels(jewels1, stones1))
print(stones_and_jewels(jewels2, stones2))