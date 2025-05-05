def is_leap_year(year):
    leap = False
    if year % 400 == 0:
        print(f'{year} is a leap year')
    elif year % 100 == 0:
        print(f'{year} is not a leap year')
    elif year % 4 == 0:
        print(f'{year} is a leap year')


year = int(input("Please enter a year of choice:"))
is_leap_year(year)

