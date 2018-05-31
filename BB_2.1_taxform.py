"""
Program: BB-Chapter2_Number1.py
Project 2.1
Compute a person's income tax.
1. Significant constants
 tax rate
 standard deduction
 deduction per dependent
2. The inputs are
 gross income
 number of dependents
3. Computations:
 net income = gross income - the standard deduction -
 a deduction for each dependent
 income tax = is a fixed percentage of the net income
4. The outputs are
 the income tax, rounded to two figures
"""
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
print("The income tax is $" + str((round(incomeTax))))
input('Press ENTER to exit')
