#check if a number is odd or even

number = input("Enter a number: ")

#checking if the modulus of the number is 0
if(int(number)%2 == 0):
    print("The number", number, "is even")

else:
    print("The number", number,  "is odd")
