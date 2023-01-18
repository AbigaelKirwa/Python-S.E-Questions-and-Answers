# find the area of a circle given the radius

rad = int(input("Enter the radius of the circle "))

def findrad(rad):
    PI = 3.142
    area = PI * (rad**2)
    return area

print("The area of the circle is ", findrad(rad))