# Task 1: Check if a Number is Even or Odd

# Ask the user to enter an integer
try:
    number = int(input("Enter an integer: "))

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
