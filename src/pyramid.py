while True:
    user_input = input("Enter the number of rows (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("\nGoodbye!\n")
        break

    try:
        print()
        
        rows = int(user_input)

        if rows > 0:
            for i in range(1, rows + 1):
                print(" " * (rows - i) + "*" * (2 * i - 1))
        elif rows < 0:
            rows = abs(rows)
            for i in range(rows, 0, -1):
                print(" " * (rows - i) + "*" * (2 * i - 1))
        else:
            print()

        print()

    except ValueError:
        print("Invalid input. Please enter a valid integer or 'exit'.\n")
