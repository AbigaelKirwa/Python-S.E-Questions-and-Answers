#find the vowels in a string

# this is the first method

"""
def findVowels(string_ent):
    listed = []
    for i in string_ent:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            listed.append(i)
        else:
            continue   

    for j in listed:
        num_of_times = listed.count(j)
        if num_of_times > 1:
            listed.remove(j)
        else:
            continue

    return listed
"""

#this is the second better method

def findVowels(string_ent):
    return [each for each in string_ent if each in "aeiou"]
 

string_choice = input("Enter your string of choice ")
print("The listed vowels in your string are ", findVowels(string_choice))