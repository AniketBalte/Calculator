def main():
    print("Welcome to the Simple Calculator!")

    # Get user input for the first number
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Get user input for the second number
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Get user choice for the arithmetic operation
    print("Choose the operation you want to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the number corresponding to the operation: ")

    # Perform the chosen arithmetic operation
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        # Check for division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = '/'
    else:
        print("Invalid choice. Please select a valid operation.")
        return

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
