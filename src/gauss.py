def numbers_sum(n):
    return n * (n + 1) // 2

def squares_sum(n):
    return n * (n + 1) * (2 * n + 1) // 6

def cubes_sum(n):
    return numbers_sum(n) ** 2

while True:
    print("\nSummation Calculator")
    print("--------------------")
    print("1. Sum of Numbers")
    print("2. Sum of Squares")
    print("3. Sum of Cubes")
    print("4. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            n = int(input("n: "))
            if n < 0:
                print("\nThe number must be a positive integer or zero!")
            else:
                print("\nSum:", numbers_sum(n))
            
        elif choice == "2":
            n = int(input("n: "))
            if n < 0:
                print("\nThe number must be a positive integer or zero!")
            else:
                print("\nSum:", numbers_sum(n))

        elif choice == "3":
            n = int(input("n: "))
            if n < 0:
                print("\nThe number must be a positive integer or zero!")
            else:
                print("\nSum:", numbers_sum(n))

        elif choice == "4":
            print("Goodbye!")
            print()
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("\nInvalid number!")