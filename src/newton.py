def root_approx(n, epsilon=1e-6):
    if n < 0:
        raise ValueError("Square root is undefined for negative numbers")

    if n == 0:
        return 0

    x = n / 2

    while abs(x * x - n) > epsilon:
        x = (x + n / x) / 2

    return x

while True:
    print("\nSquare Root Approximation")
    print("-------------------------")
    print("1. Approximate Square Root")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            n = float(input("n: "))

            if n < 0:
                print("\nThe number must be a positive number or zero!")
            else:
                print("\nSquare Root:", root_approx(n))

        elif choice == "2":
            print("Goodbye!")
            print()
            break

        else:
            print("Invalid choice!")

    except ValueError as e:
        print(e if str(e) else "\nInvalid number!")