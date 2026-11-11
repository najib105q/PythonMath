def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def derangements(n):
    total = 0

    for i in range(n + 1):
        total += (-1) ** i / factorial(i)

    return int(factorial(n) * total)

def permutations(n, k):
    if n < k or k < 0:
        return 0
    else:
        return factorial(n) // factorial(n - k)

def combinations(n, k):
    if n < k or k < 0:
        return 0
    else:
        return factorial(n) // (factorial(k) * factorial(n - k))

while True:
    print("\nCombinatorics Calculator")
    print("------------------------")
    print("1. Factorial")
    print("2. Derangements")
    print("3. Permutations")
    print("4. Combinations")
    print("5. Quit")

    choice = input("\nChoice: ")
    print()

    try:
        if choice == "1":
            n = int(input("n: "))
            print("\nFactorial:", factorial(n))

        elif choice == "2":
            n = int(input("n: "))
            print("\nDerangements:", derangements(n))

        elif choice == "3":
            n = int(input("n: "))
            k = int(input("k: "))
            print("\nPermutations:", permutations(n, k))

        elif choice == "4":
            n = int(input("n: "))
            k = int(input("k: "))
            print("\nCombinations:", combinations(n, k))

        elif choice == "5":
            print("Goodbye!\n")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid number!")