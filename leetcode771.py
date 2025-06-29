'''You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
'''

## check character in jewels
## if yess increase count by 1 and return count
def match(jewels,stones):
    count = 0
        # jewels = list()
    for ch in stones:
        if ch in jewels:
            count += 1
    return count 



jewels = "aA"
stones = "aAAbbbb"
print(match(jewels,stones))
