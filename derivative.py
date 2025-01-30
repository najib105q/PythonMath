import math

def f(x):
    return x**3 - 5*x**2 + 7*x - 10

def derivative(f, x):
    return round(((f(x + 1e-6) - f(x)) / 1e-6), 4)

print(derivative(f, 4))