# a program to print the prime numbers in a given range
def printPrime(num1, num2):
    listed = []
    for i in range(num1, num2):
        if(int(i)>0):
            if((int(i)!= 1) and (int(i)!=2) and (int(i)!=3)):
            
            # THIS ALSO WORKS
            # if(((int(number))%2 != 0) and ((int(number))%3 != 0)):
            #     print("This is a prime number")
            # else:
            #     print("This is not a prime number")
            
                if(((int(i))%2 == 0) or ((int(i))%3 == 0)):
                    continue
                else:
                    listed.append(i)
            else:
                listed.append(i)
        else:
            print("Enter a positive number please")

    return listed

number1 = int(input("Enter the first number in the range "))
number2 = int(input("Enter the second number in the range "))

print(printPrime(number1, number2))
