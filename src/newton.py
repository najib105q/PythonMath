def root_approx(n, epsilon=1e-6):
    if n < 0:
        raise ValueError("Square root is undefined for negative numbers")

    x = n / 2
    
    while abs(x * x - n) > epsilon:
        x = (x + (n / x)) / 2

    return x

print(root_approx(2))
print(root_approx(15))
print(root_approx(50))
print(root_approx(99))