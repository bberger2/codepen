##Program: population.py
##Project 3.5
##Predict popultation growth, assuming that no
##organisms die.
##Inputs:
## initial number of organisms
## rate of growth (a float > 1)
## the number of hours to achieve the rate
## number of hours of growth

initial = int(input("Enter the initial number of organisms: "))
rate = float(input("Enter the rate of growth [a real number > 1]: "))
##Gets the initial values and rate of growth
if rate < 1:
            print("Number must be greater than 1")
            input('Press ENTER to exit')
##If the rate is less then one the program ends.
else:
    needed = int(input("Enter the number of hours to achieve the rate of growth: "))
    total = int(input("Enter the total hours of growth: "))
##Gets the rest of the values
population = initial * (rate * (total / needed))
##Formula to find the population
print("The total population is", population)
input('Press ENTER to exit')
