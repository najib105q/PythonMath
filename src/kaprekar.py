def kaprekar_routine(n):
    if len(str(n).zfill(4)) != 4:
        raise ValueError("Enter a 4-digit number")

    steps = 0

    while n != 6174:
        digits = str(n).zfill(4)

        high = int("".join(sorted(digits, reverse=True)))
        low = int("".join(sorted(digits)))

        n = high - low

        print(f"{high:04d} - {low:04d} = {n:04d}")

        steps += 1

        if n == 0:
            print("All digits are identical.\n")
            return

    print(f"\nYou've reached Kaprekar's Constant in {steps} steps.\n")

kaprekar_routine(6174)
kaprekar_routine(1234)
kaprekar_routine(1875)
kaprekar_routine(1111)
kaprekar_routine(1)