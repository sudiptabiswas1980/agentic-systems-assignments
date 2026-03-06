try:
    # 1. Take name and age inputs
    name = input("Enter your name: ")
    age_input = input("Enter your age: ")

    # 2. Convert age to integer
    age = int(age_input)

    # 3. Validation for negative numbers
    if age < 0:
        print("Age cannot be negative")
    else:
        # 4. Success: Greet and categorize
        print(f"Hello {name}")

        # Age Categorization
        if age < 13:
            print("You are a Child")
        elif 13 <= age <= 17:
            print("You are a Teenager")
        elif 18 <= age <= 59:
            print("You are an Adult")
        else:
            print("You are a Senior Citizen")

        # Voting Eligibility
        if age >= 18:
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")

except ValueError:
    # Triggered if age_input is not a whole number
    print("Invalid age input")