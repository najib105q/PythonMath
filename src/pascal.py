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

print(draw_triangle(generate_pascal_triangle(5)))