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


while True:
    user_input = input("Enter a positive integer (or 'q' to quit): ")

    if user_input.lower() in ("q", "quit", "exit"):
        print("Goodbye!")
        break

    try:
        num = float(user_input)

        if not num.is_integer():
            print("Error: Please enter a whole number.")
            continue

        num = int(num)

        if num <= 0:
            print("Error: Please enter a positive integer.")
            continue

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

    except ValueError:
        print("Error: Invalid input.")