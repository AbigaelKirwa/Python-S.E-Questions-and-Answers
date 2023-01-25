def extractnum(string_input):

    numbers = [int(i) for i in string_input.split() if i.isdigit()]
    return str(numbers)

string_input = input("Enter a string ")
print("The numbers in the string are :", extractnum(string_input))