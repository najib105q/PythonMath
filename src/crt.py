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
        raise ValueError("Inverse does not exist")

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

mods = [5, 6, 7]
rems = [1, 5, 3]

x = chinese_remainder(mods, rems)

print("Solution:", x)
