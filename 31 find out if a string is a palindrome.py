#this program checks if a word is a palindrome

def panlindromechecker(str_ent):
    reversed_word = str_ent[::-1]
    if str_ent == reversed_word:
        print("The word ", str_ent ," is a palindrome")
    else:
        print("The word ", str_ent ,"is not a palindrome")

str_ent = input("Enter a word ")
print(panlindromechecker(str_ent))