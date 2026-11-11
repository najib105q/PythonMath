def collatz(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        sequence.append(n)

    return sequence

while True:
    print("\nCollatz Conjecture")
    print("------------------")
    print("1. Generate Sequence")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            n = int(input("n: "))

            if n < 1:
                print("\nn must be positive!")
            else:
                print()
                print(*collatz(n), sep=" -> ")

        elif choice == "2":
            print("Goodbye!\n")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid number!")