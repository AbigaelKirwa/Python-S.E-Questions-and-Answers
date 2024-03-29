"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

def longestCommonPrefix(strs):
    #if the array is empty we return ""
    if not strs:
        return ""
    
    #defining the item with the least length in the array
    min_str=min(strs, key=len)

    #defining an array that loops over items in the array
    for i in range(len(min_str)):
       for string in strs:
           if string[i] != min_str[i]:
               return min_str[:i]
           
    return min_str

example_array=["dream", "dracula", "dread"]
print("The longest common prefix is", longestCommonPrefix(example_array))

