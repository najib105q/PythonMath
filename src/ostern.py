def easter_date(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    
    day = 22 + d + e
    if day > 31:
        return day - 31, 4 
    else:
        return day, 3

print(easter_date(2024))
print(easter_date(2025))
print(easter_date(2026))