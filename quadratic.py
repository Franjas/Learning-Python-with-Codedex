# Create a program that asks the user for three numbers (a, b, c) and calculates the two roots using the quadratic formula:

a = float(input('Enter a > 0: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

if a != 0:

    x1 = (-b+(((b**2)-(4*a*c))**0.5))/(2*a)
    x2 = (-b-(((b**2)-(4*a*c))**0.5))/(2*a)

    print('The value of x1 is:', x1)
    print('The value of x2 is:', x2)
    
if a == 0:
    print("The value of 'a' has to be > 0")