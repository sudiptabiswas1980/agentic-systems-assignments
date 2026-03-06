try:
    # 1. Take name inputs
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # 2. Take age input and convert
    age_input = input("Enter your age: ")
    age = int(age_input)

    # 3. Check for negative age
    if age < 0:
        print("Age cannot be negative")
    else:
        # 4. Success: Print full name and next year's age
        # Using string concatenation with '+'
        full_name = first_name + " " + last_name
        print("Full Name: " + full_name)
        
        # Calculate and print age next year
        print(f"You will be {age + 1} next year")

except ValueError:
    # Triggered if int() fails (e.g., inputting "twenty")
    print("Invalid age input")