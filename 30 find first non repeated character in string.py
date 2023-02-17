#this is a program to find the first non-repeated character in a string

def first_non_repeated_character(str_ent):
    index = 0
    str = ""

    for i in str_ent:
        if str_ent.count(i) == 1:
            str += i
            break
        else: 
            index +=1
            continue
    if index >= len(str_ent):
        print("Either all characters are repeating or string is empty")
    else:
        print("First non-repeating character is ", str)


str_ent = input("Enter your string of choice ")
print(first_non_repeated_character(str_ent))