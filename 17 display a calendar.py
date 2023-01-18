# display the days in a given month and year

import calendar

year = int(input("Enter the year "))
month = int(input("Enter the month "))

def cal(month, year):
    print(calendar.month(year, month))

cal(month, year)
