# swap two numbers that have been input

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

print("The original first number was ", num1)
print("The original second number was ", num2)

def swap_number(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp

    print("After swapping, the first number is ", num1)
    print("After swapping, the second number is ", num2)

swap_number(num1, num2)