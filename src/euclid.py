def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

def lcm(a,b):
    return (a * b)/(gcd(a,b))

print(gcd(15,20))
print(lcm(15,20))