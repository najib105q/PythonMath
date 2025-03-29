def numbers_sum(n):
    return (n * (n+1))/2

def squares_sum(n):
    return (n * (n+1) * (2*n+1))/6

def cubes_sum(n):
    return numbers_sum(n)**2

print(numbers_sum(10))
print(squares_sum(10))
print(cubes_sum(10))