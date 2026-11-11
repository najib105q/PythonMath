def solve_linear_equations(coefficients, constants):
    num_equations = len(coefficients)
    num_variables = len(coefficients[0])

    for pivot_row in range(num_equations - 1):
        pivot_element = coefficients[pivot_row][pivot_row]

        if pivot_element == 0:
            raise ValueError("\nNo unique solution!")

        for row in range(pivot_row + 1, num_equations):
            factor = coefficients[row][pivot_row] / pivot_element

            for col in range(pivot_row, num_variables):
                coefficients[row][col] -= factor * coefficients[pivot_row][col]

            constants[row] -= factor * constants[pivot_row]

    for row in range(num_equations):
        if all(value == 0 for value in coefficients[row]):
            if constants[row] == 0:
                raise ValueError("\nInfinitely many solutions!")
            else:
                raise ValueError("\nNo solution!")

    solution = [0] * num_equations

    for row in range(num_equations - 1, -1, -1):
        solution[row] = constants[row]

        for col in range(row + 1, num_variables):
            solution[row] -= coefficients[row][col] * solution[col]

        if coefficients[row][row] == 0:
            raise ValueError("\nNo unique solution!")

        solution[row] /= coefficients[row][row]

    return solution

while True:
    print("\nLinear Equation Solver")
    print("----------------------")
    print("1. Solve System")
    print("2. Quit")

    choice = input("\nChoice: ")
    print()

    try:
        if choice == "1":
            n = int(input("Number of variables: "))

            if n < 1:
                print("\nNumber of variables must be positive!")
                continue

            coefficients = []
            constants = []

            print()

            for i in range(n):
                row = list(map(float, input(f"Equation {i + 1}: ").split()))

                if len(row) > n:
                    raise ValueError("Too many coefficients")

                while len(row) < n:
                    row.append(0)

                coefficients.append(row)

            print()

            for i in range(n):
                constants.append(float(input(f"Constant {i + 1}: ")))

            solution = solve_linear_equations(coefficients, constants)

            print("\nSolution:\n")

            for i in range(n):
                print(f"x{i + 1} = {round(solution[i], 6)}")

        elif choice == "2":
            print("Goodbye!\n")
            break

        else:
            print("\nInvalid choice!")

    except ValueError as e:
        print(e if str(e) else "\nInvalid input!")