# generate a multiplication table given a number

table_number = int(input("Enter a number and obtain its multiplication table "))

def multiplication(table_number):
    for i in range(1, 11):
        mult = i * table_number
        print(table_number, " * ", i, " = ", mult)

multiplication(table_number)