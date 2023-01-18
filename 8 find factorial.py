# find the factorial of a number


# 1) USING A PYTHON BUILT IN FUNCTION

# import math

# def factorial(num):
#     return(math.factorial(num))

# num = int(input("Input the number whose factorial you want to find "))
# print("The factorial of the number you entered is ", factorial(num))

# 2) USING ITERACTION
# def factorial(num):
#     fact = 1
#     if(num<0):
#         print("There are no factorials of negative numbers")
#     elif(num==0):
#         print("The factorial of zero is one")
#     else:
#         for i in range(1,num+1):
#             fact = fact*i
#         print(f"The factorial of the number is ", fact)

# num =int(input("Enter a number to find its factorial "))
# factorial(num)


# 3) USING FACTORIAL
def recur_factorial(num):
    if(num == 1):
        return num
    else:
        return num*recur_factorial(num-1)

num=int(input("Enter the number whose factorial you want to see "))

if (num<0):
    print("sorry factorial does not exist for negative numbers")

elif (num==0):
    print("The factorial of the number is 1")

else:
    print("The factorial of the number is ", recur_factorial(num))