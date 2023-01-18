# calculate the area of a given triangle

def triangleArea(len1, len2, len3):
    #sp = semi perimeter of the triangle
    sp = (len1 + len2 + len3)/2

    area = (sp*(sp-len1)*(sp-len2)*(sp-len3))**0.5
    return round(area, 3)

len1=int(input("Enter the first length of the triangle "))
len2=int(input("Enter the second length of the triangle "))
len3=int(input("Enter the third length of the triangle "))

print("The area of the triangle is ", triangleArea(len1, len2, len3))

