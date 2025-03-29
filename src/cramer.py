def solve_linear_equations(coefficients, constants):
    num_equations = len(coefficients)
    num_variables = len(coefficients[0])

    for pivot_row in range(num_equations - 1):
        pivot_element = coefficients[pivot_row][pivot_row]
        for row in range(pivot_row + 1, num_equations):
            factor = coefficients[row][pivot_row] / pivot_element
            for col in range(pivot_row, num_variables):
                coefficients[row][col] -= factor * coefficients[pivot_row][col]
            constants[row] -= factor * constants[pivot_row]

    solution = [0] * num_equations
    for row in range(num_equations - 1, -1, -1):
        solution[row] = constants[row]
        for col in range(row + 1, num_variables):
            solution[row] -= coefficients[row][col] * solution[col]
        solution[row] /= coefficients[row][row]

    return solution

coefficients = [[3, 2, 1], [2, 1, -1], [2, -1, 2]]
constants = [10, 1, 6]
solution = solve_linear_equations(coefficients, constants)

print("Solution:")
print("x =", round(solution[0]))
print("y =", round(solution[1]))
print("z =", round(solution[2]))