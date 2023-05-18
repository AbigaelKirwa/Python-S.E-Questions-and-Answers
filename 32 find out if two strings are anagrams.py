#anagrams are words that have the same characters but in different orders

def anagram(str_a, str_b):
    count = 0
    # loop checks if all letters in first string are in second string
    for i in str_a:
        if i in str_b:
            count = count + 1
        else:
            break
    if count == len(str_b) and count == len(str_a):
        print("These strings are anagrams")
    else:
        print("These strings are not anagrams")


text_one = input("Enter first string to check if anagram ")
text_two = input("Enter second string to check if anagram ")

anagram(text_one, text_two)

