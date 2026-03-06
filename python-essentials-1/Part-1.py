try:
    # Take user input
    val1 = input("Enter first number: ")
    val2 = input("Enter second number: ")

    # Convert to integers
    num1 = int(val1)
    num2 = int(val2)

    # Perform operations
    print(f"Sum: {num1 + num2}")
    print(f"Division: {num1 / num2}")

except ValueError:
    # Triggered if int() fails (e.g., inputting "abc" or "10.5")
    print("Invalid input")

except ZeroDivisionError:
    # Triggered if num2 is 0 during the division operation
    print("Cannot divide by zero")