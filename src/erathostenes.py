def filter_primes(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    primes = [i for i in range(2, n + 1) if prime[i]]
    return primes

print(filter_primes(100))