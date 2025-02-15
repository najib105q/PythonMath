def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a,b)

print(swap(19,25))