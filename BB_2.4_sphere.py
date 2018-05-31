import math
pi = math.pi
radius = int(input("Enter the radius : "))
diameter = radius * 2
circumference = 2 * pi * radius
surfaceArea = 4 * pi * (math.pow(radius , 2))
volume = (4/3) * pi * (math.pow(radius, 3))
print("The diameter is", diameter)
print("The circumference is", circumference)
print("The surface area is", surfaceArea)
print("The volume is", volume)
input('Press ENTER to exit')
