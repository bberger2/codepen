##Program: guess.py
##Project 3.3
##The computer guesses the user's number using the minimum
##number of attempts

import random
while True:
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))
    myNumber = int(input("Enter the number:"))
    ##Determine the value of the numbers
    count = 1
    computernumber = random.randint(smaller, larger)
    ##Computer makes its first guess
    print("The computers first guess was", computernumber)
    while True:
        if computernumber < myNumber:
            smaller = computernumber
            computernumber = random.randint(smaller, larger)
            count += 1
            print("Computer guessed", computernumber)
            continue
        #If the computers number is too low it sets that number as the lowest possible number it could guess and tries again
        elif computernumber > myNumber:
            larger = computernumber
            computernumber = random.randint(smaller, larger)
            count += 1
            print("Computer guessed", computernumber)
            continue
        #If the computers number is too high it sets that number as the highest possible number it could guess and tries again
    
        else:
            print("Computer guessed the correct number in", count, "tries!")
            break
    ##Computer guessed correctly game over
    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print ('Invalid input.')
    if answer == 'y':
        continue
    else:
        print ('Goodbye')
        break
##code to reset
