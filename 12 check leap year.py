#check if a year entered is a leap year

year = int(input("Enter a given year and check whether it is a leap year "))

def leap_year(year):
    if (year%4 == 0):
        print("The year ",year, " was a leap year")
    else:
        print("The year ",year, " was not a leap year")

leap_year(year)

