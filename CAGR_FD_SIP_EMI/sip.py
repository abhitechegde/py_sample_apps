# FV = ( P * ((1+i)^n-1)/i) * (1+i)
# i = r/100/12 or 0.01   r=12% ; for 12 months (anually)
# Where:
# FV= future value
# P = amount invested at the start of every payment interval
# n = number of payments
# i = periodic interest rate
# r = expected annual returns (P.A %)
# You must enter the amount of investment, frequency of investment, duration of investment, and the expected returns
# Example you invest Rs 1,500 per month for 60 months. (5years)
# You expect a 12% annual rate of return (r).
# You have i = r/100/12 or 0.01.
# FV = 2000 * [(1+0.01) ^60 - 1] * (1+0.01)/0.01
# You get Rs 123730 at maturity

import math

P=float(input("Enter Monthly Investment: "))
n=12 * (int(input("Enter Time Period (In Years): ")))
r= float(input("Enter Expected rate of return: "))
i= r/100/12
FV = math.ceil(( P * ((1+i)**n-1)/i) * (1+i))
print("Total amount invested: {} You get Rs {} at maturity.".format((P*n),FV))
print("You Earned: %s Extra" %(FV-(P*n)))

