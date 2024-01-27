numbers = []

while True:
    user_input = input("Enter a positive number (enter a non-positive number to stop): ")

    # Check if the input can be converted to a float and is non-negative
    if user_input.replace('.', '', 1).isdigit() and float(user_input) > 0:
        numbers.append(float(user_input))
    elif user_input.replace('-', '', 1).isdigit() and float(user_input) <= 0:
        break  # Exit the loop if a non-positive number is entered
    else:
        print("Invalid input. Please enter a valid positive number.")

# Data handling after the loop
if numbers:
    print(f"You entered the following positive numbers: {numbers}")
else:
    print("No positive numbers were entered.")