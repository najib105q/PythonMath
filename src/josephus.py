'''
A king orders a crowd of prisoners to execute themselves by building a circle
where each person should kill his next living neighbour with higher number.
'''
import math

def josephus(n):
    m = int(math.log2(n))
    l = n - 2**m
    return 2*l + 1

print(josephus(1))
print(josephus(2))
print(josephus(3))
print(josephus(16))
print(josephus(41))
print(josephus(100))
