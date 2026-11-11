"""
Kaprekar Routine

Kaprekar's Routine applies to four-digit numbers with at least two distinct
digits.

Steps:
    1. Arrange the digits in descending order.
    2. Arrange the digits in ascending order.
    3. Subtract the smaller number from the larger number.
    4. Repeat the process.

The routine always reaches Kaprekar's Constant:

    6174

Examples:
    1234 -> 6174
    1875 -> 6174
    6174 -> 6174

Numbers with all identical digits eventually reach:

    0000

and do not reach 6174.
"""


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
            print("\nAll digits are identical!")
            return

    print(f"You've reached Kaprekar's Constant in {steps} steps.")

while True:
    print("\nKaprekar Routine")
    print("----------------")
    print("1. Apply Routine")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            n = int(input("4-digit number: "))

            if n < 0 or n > 9999:
                print("\nThe number must be positive and have at most 4 digits!")
            else:
                print()
                kaprekar_routine(n)

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice!")

    except ValueError as e:
        print(f"\n{e}")