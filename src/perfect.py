def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

for p in range(2, 20):
    mersenne = 2**p - 1

    if is_prime(mersenne):
        perfect = 2**(p - 1) * mersenne
        print(perfect)