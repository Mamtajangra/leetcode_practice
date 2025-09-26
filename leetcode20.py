'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
'''


'''   ## define a stack
        ## check the pair of braces if yess then append to stack
        ## if any bracket not present in stack or if we pop the top bracket and unable to find its match in stack return false
        ## continue the loop upto which stack become empty because all pairs are removed'''

def valid(s):
    stack = []
    for b in s:
            if b =="(":
                stack.append(")")
            elif b == "{":
                stack.append("}")
            elif b == "[":
                stack.append("]")
            else:
                if not stack or stack.pop()!= b:
                    return False    
    return not stack


s = "()[]{}"
print(valid(s))
