def calculating(a, b, c):
    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == 'x':
        result = a * b
    return result
    
print("Welcome to ICS 32 PyCalc!")
n1 = int(input("Enter your first number:"))
n2 = int(input("Enter your second number:"))
operator = input("Enter your desired operator (+, -, or x):")
total = calculating(n1, n2, operator)
print("The result of the calculation is:", total)
