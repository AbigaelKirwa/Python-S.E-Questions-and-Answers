#check if number entered is a prime number

def primeNumbers(number):

    if(int(number)>0):
        if((int(number)!= 1) and (int(number)!=2) and (int(number)!=3)):
            
            # THIS ALSO WORKS
            # if(((int(number))%2 != 0) and ((int(number))%3 != 0)):
            #     print("This is a prime number")
            # else:
            #     print("This is not a prime number")
            
            if(((int(number))%2 == 0) or ((int(number))%3 == 0)):
                print("This is not a prime number")
            else:
                print("This is a prime number")
        else:
            print("This is a prime number")
    else:
        print("Enter a positive number please")

number = int(input("Input a number: "))
primeNumbers(number)