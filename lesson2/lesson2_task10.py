def bank(vklad, years):
     
     for _ in range(years):
        vklad = vklad * 1.1
     return vklad

vklad = int(input("первоначальная сумма вклада: "))
years = int(input("срок вклада(годы): ")) 

result = bank(vklad, years)

print("вклад составит", result,"руб", "через", years, "лет")