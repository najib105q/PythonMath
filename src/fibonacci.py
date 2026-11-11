def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def binet(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2

    return round((phi ** n - psi ** n) / 5 ** 0.5)

while True:
    print("\nFibonacci Calculator")
    print("--------------------")
    print("1. Calculate")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            n = int(input("n: "))

            if n < 1:
                print("\nThe number must be positive!")
            else:
                print("\nRecursive:", fib(n))
                print("Binet:", binet(n))

        elif choice == "2":
            print("Goodbye!\n")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("\nInvalid number!")