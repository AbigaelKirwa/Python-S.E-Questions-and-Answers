"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

def isValid(s):
    # if the string has zero items or one item, then we return a false automatically
    if len(s)==1 or len(s)==0:
        return False
    else:
        # we iterate over all the characters of the string and check if opening brackets are next to closing brackets
        for i in range(len(s)):
            if(s[i]=="(") and (s[(i+1)]==")") :
                return True
            elif (s[i]=="[") and (s[(i+1)]=="]"):
                return True
            elif (s[i]=="{") and (s[(i+1)]=="}"):
                return True
            else:
                return False
        
d="(])"
print(isValid(d))


