def collatz(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        sequence.append(n)

    return sequence

print(*collatz(1), sep=" -> ")
print(*collatz(3), sep=" -> ")
print(*collatz(16), sep=" -> ")
print(*collatz(27), sep=" -> ")