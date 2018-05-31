##Program: leibniz.py
##Project 3.6
##This program approximates the value of pi using an algorithm
##designed by the German mathematician Gottfried Leibniz. The
##algorithm is as follows:
##pi = 4 - 4 / 3 + 4 / 5 - 4 / 7 + . . .
##This program allows the user to specify the number of iterations
##to use in the approximation.

import math
computerpi = math.pi
##Sets the computers estimation for pi to be used as comparison
iterations = int(input("Enter the number of iterations: "))
iterations -= 2 ##I may have done something wrong with the formula because it always gave me the answer two iterations in advance. This line solved that.
denominator = 1
addto = 1

for i in range(iterations): ##This will loop for the set amount of iterations
    denominator += 2 ##Adds two to the denominator like in the given equation
    addto -= (1/denominator) ##Adds the next part of the equation, after the first iteration (1) you subtract it by 1/3 which is one over the denomator (3)
    denominator += 2
    addto += (1/denominator)
    ##repeats the two lines above, adding instead of subtracting just like the equation given.

pi = addto * 4 ##Pi in the equation was being divided by 4, so multiplying the final answer would give the approximation

print("The approximation of pi is", pi)
print("Compare this to the computers estimation:", computerpi)
##Prints the final answers
input('Press ENTER to exit')
