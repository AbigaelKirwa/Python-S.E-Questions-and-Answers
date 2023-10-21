#check if number entered is a prime number

#not correct

def primeNumbers(number):

    # we first ensure the number is greater than 1
    if(int(number)>1):
        # if the number is 2 or 3, then it is definitely a prime number
        if(number == 2 or number == 3):
            print(number, " is a prime number")
        else:
            # if a number between 2 and half the number divides it and has a modulo of 0 then it is prime
            # e.g if the number is 17 then range is (2,9) so if any number between 2 and 9 divides it perfectly then it is not a prime number
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