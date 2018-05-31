##Program: equilateral.py
##Project 3.1
##Determine whether or not three input sides compose an
##equilateral triangle

first = int(input("Enter first side: "))
second = int(input("Enter second side: "))
third = int(input("Enter third side: "))
##Determine the value of the sides

if first == second == third:
    print("This is an equilateral triangle")
##If the sides are all the same the triangle is equilateral
else:
    print("This is not an equilateral triangle")
input('Press ENTER to exit')
