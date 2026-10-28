def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

def primitive_triples(limit):
    for m in range(2, limit+1):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m - n) % 2 == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                print(a, b, c)

primitive_triples(10)