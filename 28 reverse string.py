# write a program to reverse a string

def strReverse(str_ent):
    return str_ent[::-1]

str_ent = input("Write a string of your choice and have it reversed ")
print ("The reversed string is ", strReverse(str_ent))



"""
def strReverse(str_ent):
    reversed_str = ''
    index = len(str_ent)

    while index:
        index -= 1
        reversed_str += str_ent[index]

    return reversed_str

str_ent = input("Write a string of your choice and have it reversed ")
print ("The reversed string is ", strReverse(str_ent))
"""