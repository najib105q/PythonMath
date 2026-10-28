def is_happy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return n == 1

for n in range(1, 101):
    if is_happy(n):
        print(n)