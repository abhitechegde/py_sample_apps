# CAGR= (L/F)^(1/N) -1
# Where:
# F = first value in your series of Values.
# L = last value in your series of values.
# N = number of years between your first and last value in your series of values.

F = float(input("Enter The Initial Value: "))
L = float(input("Enter The Final Value: "))
N = int(input("Enter The Total Number OF Years: "))

CAGR= (L/F)**(1/N) -1
print('Your Investment had a CAGR of {:.2%}'.format(CAGR))