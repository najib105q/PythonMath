def generate_pascal_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

def draw_triangle(triangle):
    width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        print(" ".join(map(str, row)).center(width))

while True:
    print("\nPascal Triangle")
    print("---------------")
    print("1. Generate Triangle")
    print("2. Quit\n")

    choice = input("Choice: ")
    print()

    try:
        if choice == "1":
            n = int(input("Rows: "))

            if n < 0:
                print("\nThe number must be a positive integer or zero!")
            elif n == 0:
                print("\nEmpty triangle")
            else:
                print()
                draw_triangle(generate_pascal_triangle(n))

        elif choice == "2":
            print("Goodbye!")
            print()
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("\nInvalid number!")