# Задание 1

year = int(input("напишите год : "))
def is_year_leap(year):
    if year % 4 == 0:
        print(True)
    else:
        print(False)
        
result = is_year_leap(year)


# Задание 2

year = int(input("напишите год : "))

def is_year_leap(year):
    if year % 4 == 0:
        print(f"год {year}:  {True}")
    else:
        print(f"год {year}:  {False}")

print(f'{is_year_leap(year)}')