while True:
    user_input = input("Enter the number of rows (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("\nGoodbye!\n")
        break

    try:
        print()
        
        rows = int(user_input)

        if rows != 0:
            for i in range(1, abs(rows) + 1):
                print(" " * (abs(rows) - i) + "*" * (2 * i - 1))
            for i in range(abs(rows), 0, -1):
                print(" " * (abs(rows) - i) + "*" * (2 * i - 1))

        print()

    except ValueError:
        print("Invalid input. Please enter a valid integer or 'exit'.\n")