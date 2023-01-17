#check if number entered is a prime number

number = input("Input a number: ")

if((int(number)!= 1) and (int(number)!=2) and (int(number)!=3)):
    
    if(((int(number))%2 != 0) and ((int(number))%3 != 0)):
        print("This is a prime number")
    else:
        print("This is not a prime number")

else:
    print("This is a prime number")