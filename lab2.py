#lab2.py

# Joana Ugarte
# joanau@uci.edu
# 44875730

def add(a, b):
    return  a + b

def sub(a, b):
    return  a - b

def div(a, b):
    return  a / b

def mul(a, b):
    return  a * b

def run():
    a = input("Enter left operand: ")
    b = input("Enter right operand: ")
    operator = input("What type of calculation would you like to perform (+, -, x, /)? ")
    
    r = 0

    if operator == "+":
        try: 
            r = add(int(a),int(b))
        except:
            print("Error occured integer not used, try again with whole number.")
            run()
    elif operator == "-":
        try:
            r = sub(int(a),int(b))
        except:
            print("Error occured integer not used, try again with whole number.")
            run()
    elif operator == "x":
        try:
            r = mul(int(a),int(b))
        except:
            print("Error occured integer not used, try again with whole number.")
            run()
    elif operator == "/":
        try:
            r = div(int(a),int(b))
        except:
            print("Error occured, use integer and make sure right operand is not 0.")
            run()
    else:
        r = "Unable to perform the desired calculation, please try again."
        
    
    print(r)
    
    if input("Run another calculation (y/n)? ") == "y":
        run()


if __name__ == "__main__":
    print("Welcome to PyCalc!")
    run()

