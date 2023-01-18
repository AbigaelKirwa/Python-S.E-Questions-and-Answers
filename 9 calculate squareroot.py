# calculate the function of a given number


# 1) USING A DEFINED FUNCTION
# def squareroot(num):
#     return (num**0.5)

# num=int(input("Enter a number whose squareroot you want to find: "))

# print(" The factorial of the number is ", squareroot(num) )

# 2) USING A PREDEFINED FUNCTION
import math

def squareroot(num):
    return math.sqrt(num)

num=int(input("Enter a number whose squareroot you want to find: "))

print(" The factorial of the number is ", squareroot(num) )
