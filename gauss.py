def sum(n):
    return (n * (n+1))/2
    
def sum2(n):
    return (n * (n+1) * (2*n+1))/6
    
def sum3(n):
    return sum(n)**2
    
print(sum(10))
print(sum2(10))
print(sum3(10))