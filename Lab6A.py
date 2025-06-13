# Lab6A.py
# A simple calculator for multiplication and exponentiation using loops

def multiply(a, b):
    result = 0
    for i in range(b):
        result = result + a
    return result

def exponent(base, power):
    result = 1
    for i in range(power):
        result = result * base
    return result

while True:
    print("1. Multiply")
    print("2. Exponentiate")
    print("3. Quit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        answer = multiply(x, y)
        print(x, "*", y, "=", answer)
    elif choice == 2:
        base = int(input("Enter the base: "))
        power = int(input("Enter the exponent: "))
        answer = exponent(base, power)
        print(base, "^", power, "=", answer)
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
