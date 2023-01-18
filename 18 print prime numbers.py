#print prime numbers in a given range

first_num = int(input("Input the first number in range "))
last_num = int(input("Input the last number in range "))

def printPrime(first_num, last_num):
    prime = []

    for i in range(first_num, last_num):
        if (i==0 or i==1 or i==2 or i==3):
            prime.append(i)

        elif((i%2 != 0) and (i%3 !=0)):
            prime.append(i)
    
    return(prime)

print("The prime numbers found in the range are ", printPrime(first_num, last_num))
