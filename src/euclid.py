def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp

    return a

def lcm(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        return (a * b) // gcd(a, b)

while True:
    print("\nGCD and LCM Calculator")
    print("----------------------")
    print("1. Calculate")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            a = int(input("First number: "))
            b = int(input("Second number: "))
            print()

            print("GCD:", gcd(a, b))
            print("LCM:", lcm(a, b))

        elif choice == "2":
            print("Goodbye!\n")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("\nInvalid number!")