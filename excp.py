print("Program starts...")


try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a / b

    print("The division of", a, "and", b, "is", c)

except Exception:
    print("Error in data")

print("Program ends...")
