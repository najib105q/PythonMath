def filter_primes(n):
    prime = [True] * (n + 1)

    if n >= 0:
        prime[0] = False

    if n >= 1:
        prime[1] = False

    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

        p += 1

    primes = []

    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)

    return primes


while True:
    print("\nPrime Number Filter")
    print("-------------------")
    print("1. Generate Primes")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            n = int(input("Upper limit: "))

            if n < 2:
                print("\nNo primes found!")
            else:
                primes = filter_primes(n)

                print("\nPrimes:")
                print(*primes)

                print(f"\nCount: {len(primes)}")

        elif choice == "2":
            print("Goodbye!\n")
            break

        else:
            print("\nInvalid choice!")

    except ValueError:
        print("\nInvalid number!")