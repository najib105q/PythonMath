"""
Josephus Problem

A king orders a crowd of prisoners to execute themselves by forming a circle.
Starting from prisoner 1, each living prisoner kills the next living prisoner.
The process repeats until only one prisoner remains.

For the special case where every second prisoner is eliminated, the survivor
can be found using the formula:

    J(n) = 2l + 1

where

    n = 2^m + l
    0 <= l < 2^m

Examples:
    J(1)   = 1
    J(2)   = 1
    J(3)   = 3
    J(16)  = 1
    J(41)  = 19
    J(100) = 73
"""

import math


def josephus(n):
    m = int(math.log2(n))
    l = n - 2 ** m

    return 2 * l + 1


while True:
    print("\nJosephus Problem")
    print("----------------")
    print("1. Find Survivor")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            n = int(input("Number of prisoners: "))

            if n <= 0:
                print("\nThe number must be a positive integer!")
            else:
                print("\nSurvivor:", josephus(n))

        elif choice == "2":
            print("Goodbye!")
            print()
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("\nInvalid number!")