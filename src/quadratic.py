def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)

        return root1, root2

    elif discriminant == 0:
        return -b / (2 * a)

    else:
        return None

while True:
    print("\nQuadratic Equation Solver")
    print("-------------------------")
    print("1. Find Roots")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))

            if a == 0:
                print("\na must not be zero!")

            else:
                result = roots(a, b, c)

                if result is None:
                    print("\nNo real roots")

                elif isinstance(result, tuple):
                    print()
                    print("Root 1:", result[0])
                    print("Root 2:", result[1])

                else:
                    print("\nRoot:", result)

        elif choice == "2":
            print("Goodbye!")
            print()
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("\nInvalid number!")