# E= (P*r*(1+r)^n)/((1+r)^n-1)
# Where:
# P = loan amount (principle amount)
# r = interest rate per month r=R/(12*100) [R= interest rate per year]
# n= loan time period in year 
import math
P = float(input("Enter the loan amount taken: "))
R = float(input("Enter rate of interest per year: "))
n = int(input("Enter number of months: "))
r = R/(12*100)
Emi = math.ceil((P*r*(1+r)**n)/((1+r)**n-1))
print("Monthly EMI amount: " +str(Emi))
print("Total amount paid is Rs {} (difference amount is Rs {})".format(Emi*n,Emi*n-P))