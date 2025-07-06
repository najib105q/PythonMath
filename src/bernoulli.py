def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def derangements(n):
    if n == 0:
        return 1
    else:
        result = 0
        for i in range(n+1):
            result += (-1)**i / factorial(i)
        return int(factorial(n) * result)

def permutations(n,k):
    return (factorial(n))/(factorial(n-k))

def combinations(n,k):
    return (factorial(n))/(factorial(k) * factorial(n-k))

print(factorial(5))
print(derangements(5))
print(permutations(9,3))
print(combinations(9,3))