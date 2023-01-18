#check if a given number is found in the fibonacci sequence

number=int(input("Enter a number to check whether it belongs in a fibonacci sequence "))
fib_nums = [0,1]

while(fib_nums[-1])<= number:
    fib_nums.append(fib_nums[-1]+fib_nums[-2])

if number in fib_nums:
    print("The number is a fibonacci number")
else:
    print("The number is NOT a fibonacci number")