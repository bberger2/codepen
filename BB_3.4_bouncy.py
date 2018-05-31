##Program: bouncy.py
##Project 3.4
##This program calculates the total distance a ball travels as it bounces
##given:
##1. the initial height of the ball
##2. its bounciness index
##3. the number of times the ball is allowed to continue bouncing

height = float(input("Enter the height from which the ball is dropped: "))
index = float(input("Enter the bounciness index of the ball: "))
bounces = float(input("Enter the number of times the ball is allowed to continue bouncing: "))
##Determine the values needed for the opreation
bounce = (height * index)
last = index * bounce
distance = height + (bounce * bounces) + last
##Determines distance by using a formula. This formula took mostly trial and error until the distance matched up with the given numbers.
print(distance)
input('Press ENTER to exit')
