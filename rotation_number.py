"""
rotation number 
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b = []
number = int(input("enter the rotation number"))
if number > 0 and number < len(a):
    b = a[-number:] + a[:-number]
else:
    print(a)

print(b)
