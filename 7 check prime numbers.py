#check if number entered is a prime number

#not correct

def primeNumbers(number):

    if(int(number)>1):
        if(number == 2 or number == 3):
            print(number, " is a prime number")
        else:
            for i in range (2, int(number/2)-1):
                if (number%i) == 0:
                    print(number, " is not a prime number")
                    break
            else:
                print(number, " is a prime number")
    else:
        print(number, " is not a prime number")
       

number = int(input("Input a number: "))
primeNumbers(number)