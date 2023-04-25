def consonantsandvowels(str_ent):
    num_vowels=0
    num_consonants=0
    var_lowered_input = str_ent.lower()
    input_len = len(var_lowered_input)

    for i in str_ent.lower():
        if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            num_vowels=num_vowels+1
        elif(i==" "or i=="1" or i=="2" or i=="3" or i=="4" or i=="5"or i=="6" or i=="7" or i=="8" or i=="9" or i=="0"):
            continue
        else:
            num_consonants=num_consonants+1
    
    print("number of vowels and consonants respectively are: ", num_vowels, " and ", num_consonants)

    

str_ent = input("Enter a string ")
print(consonantsandvowels(str_ent))


   