# find the factorial of a number


# THIS IS 
# import math

# def factorial(num):
#     return(math.factorial(num))

# num = int(input("Input the number whose factorial you want to find "))
# print("The factorial of the number you entered is ", factorial(num))


def factorial(num):
    fact = 1
    if(num<0):
        print("There are no factorials of negative numbers")
    elif(num==0):
        print("The factorial of zero is one")
    else:
        for i in range(1,num+1):
            fact = fact*i
        print(f"The factorial of the number is ", fact)

num =int(input("Enter a number to find its factorial "))
factorial(num)
