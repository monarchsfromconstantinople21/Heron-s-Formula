print("Hey! This program is to help you calculate the area of the triangle!")

print("")

num1 = int(input("Great! Enter the length of side 1:"))
print("")

num2 = int(input("Great! Enter the length of side 2:"))
print("")

num3 = int(input("Great! Enter the length of side 3:"))
print("")

total = num1 + num2 + num3

sp = total//2

sa = sp - num1
sb = sp - num2
sc = sp - num3

final = sp * sa * sb * sc

num_sqrt = final ** 0.5

print(num_sqrt)