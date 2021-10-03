# A=P(1+r/n)^n*t
# Where:
# A = maturity amount
# P = principal amount
# r = rate of interest
# t = number of years
# n = coumpounted interest frequency
import math

P = float(input("Enter the principal amount paid: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter number of years amount to be fixed: "))
# n = float(input("Enter coumpounted interest frequency: "))
# c= 1+r/n
# b=c**n
A = math.ceil(P+(P*r*t/100))
print("The total amount you will get after {} years, is {}".format(t,A))