#print prime numbers in a given range

first_num = int(input("Input the first number in range "))
last_num = int(input("Input the last number in range "))

def printPrime(first_num, last_num):
    prime = []

    for num in range(first_num, last_num + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    
    return(prime)

print("The prime numbers found in the range are ", printPrime(first_num, last_num))
