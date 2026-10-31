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

while True:
    user_input = input("Enter a year to find the date of Easter (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("\nGoodbye!\n")
        break
    
    try:
        year = int(user_input)
        month, day = easter_date(year)
        print(f"\nEaster in {year} falls on: {month}/{day}\n")
    except ValueError:
        print("\nInvalid input. Please enter a valid year or type 'exit' to quit.\n")
        break
