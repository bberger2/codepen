##Program: right.py
##Project 3.2
##Determine whether or not three input sides compose a
##right triangle.

import math
first = int(input("Enter first side: "))
second = int(input("Enter second side: "))
third = int(input("Enter hypotenuse: "))
##Determine the value of the sides
third = third + 0.5 - 0.5 ##Third would not compute correctly unless I did this for some reason.
hypotenuse = math.sqrt((first * first + second * second)) ##Calculate the hypotenuse by using the pythagorean theorum
if hypotenuse == third:
    print("The triangle is a right triangle")
else:
    print("The triangle is not a right triangle")
##Determine if the hypotenuse entered is equal to the hypotenuse calculated.
input('Press ENTER to exit')
