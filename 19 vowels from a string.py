#get the number of vowels in a string

def getVowel(String):

    vowels = set([each for each in String if each in "aeiou"])
    return(vowels)

string1 = input("Enter a string of choice ")
print("The vowels present are ", getVowel(string1))

