def sequence(n):
    if n == 1 or n == 2:
        return 1
    else: 
        return sequence(n-1) + sequence(n-2)
    
def binet(n):
    phi = (1 + 5**0.5) / 2
    psi = (1 - 5**0.5) / 2
    return round((phi**n - psi**n) / 5**0.5)
    
print(sequence(7))
print(binet(7))
