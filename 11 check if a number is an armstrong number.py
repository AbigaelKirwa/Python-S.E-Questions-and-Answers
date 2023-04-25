# this program checks if a number is an armstrong number

num = int(input("Enter a number to check if it is an armstrong number "))

sum = 0
temp = num
while (temp > 0):
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10

if (num == sum):
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
