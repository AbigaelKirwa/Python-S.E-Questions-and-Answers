# write a program to show implicit data type conversion
# in implicit conversion, data is converted from a low level data type to a high level data type such as int to float to prevent loss of data

int_num = 12
float_num = 1.2

new_num = int_num + float_num

print("The summed number is ", new_num)
print("The number is of datatype ", type(new_num))