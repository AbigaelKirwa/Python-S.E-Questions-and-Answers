#this is a program to find the first non-repeated character in a string

def first_non_repeated_character(str_ent):

    for i in str_ent:
        if str_ent.count(i) == 1:
            break
        else: 
            continue
    return i


str_ent = input("Enter your string of choice ")
print("The first non repeated character is ", first_non_repeated_character(str_ent))