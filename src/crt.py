def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)

    if gcd != 1:
        raise ValueError("\nInverse does not exist!")

    return x % m


def chinese_remainder(moduli, remainders):
    N = 1

    for m in moduli:
        N *= m

    result = 0

    for m, a in zip(moduli, remainders):
        Ni = N // m
        inverse = mod_inverse(Ni, m)

        result += a * Ni * inverse

    return result % N


while True:
    print("\nChinese Remainder Theorem")
    print("-------------------------")
    print("1. Solve System")
    print("2. Quit")

    choice = input("\nChoice: ")
    print()

    try:
        if choice == "1":
            n = int(input("Number of congruences: "))

            if n < 1:
                print("\nNumber of congruences must be positive!")
                continue

            moduli = []
            remainders = []

            print()

            for i in range(n):
                moduli.append(int(input(f"Modulus {i + 1}: ")))

            print()

            for i in range(n):
                remainders.append(int(input(f"Remainder {i + 1}: ")))

            solution = chinese_remainder(moduli, remainders)

            print("\nSolution:", solution)

        elif choice == "2":
            print("Goodbye!\n")
            break

        else:
            print("\nInvalid choice!")

    except ValueError as e:
        print(e if str(e) else "\nInvalid input!")