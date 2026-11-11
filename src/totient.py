def prime_factorization(n):
    factors = {}
    d = 2

    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors


def totient(n):
    if n == 1:
        return 1

    result = n

    for prime in prime_factorization(n):
        result = result * (prime - 1) // prime

    return result


def get_positive_integer():
    while True:
        user_input = input("Enter a positive integer: ")

        try:
            num = float(user_input)

            if not num.is_integer():
                print("Error: Please enter a whole number.")
                continue

            num = int(num)

            if num <= 0:
                print("Error: Please enter a positive integer.")
                continue

            return num

        except ValueError:
            print("Error: Invalid input.")


while True:
    print("\nNumber Theory Toolkit")
    print("1. Prime Factorization")
    print("2. Euler Totient Function")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        num = get_positive_integer()

        if num == 1:
            print("1 = 1")
            continue

        factors = prime_factorization(num)

        parts = []
        for prime, exponent in factors.items():
            if exponent == 1:
                parts.append(str(prime))
            else:
                parts.append(f"{prime}^{exponent}")

        print(f"{num} = {' × '.join(parts)}")

    elif choice == "2":
        num = get_positive_integer()
        print(f"φ({num}) = {totient(num)}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Error: Invalid choice.")