def calculate_easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19 * a) + 24) % 30
    e = ((2 * b) +  (4 * c) + (6 * d) + 5) % 7
    f = 22 + d + e
    day = f % 32
    if f > 31 :
        month = 4
    else :
        month = 3
    return day, month
print(calculate_easter(2024))