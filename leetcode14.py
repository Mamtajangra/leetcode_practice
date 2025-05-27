'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''


''' here we want to find the common values in string so we fixed initialy first string value and trying to compare this with other
if it match with other increase one and return result in the way siuch that ---- jb hmne flower ko fix kiya uspe loop lgaya to har alphabet ko i se btaya
aur unko curr value se denote kiya fir dusra ;loop lga usmehmm sabhi char value le rahe hai jaise flow,flight agar inke alphabets unequal hai to 
result same rahega otherwise result mein hmm common ko daal denge '''
def common_prefix(strs):
    start = strs[0]
    result = ""
    for i in range(len(start)):
        #every alphabet is current
        curr = start[i]
        ## ab hmm har ek list value ko le rahe hai jo 1 ke baad hai kyunki zero ko fix kardiya
        for char in strs[1:]:
            if char[i] != curr:
                return result
    
        result = result + curr
    return result




strs = ["flower","flow","flight"]
print(common_prefix(strs))



