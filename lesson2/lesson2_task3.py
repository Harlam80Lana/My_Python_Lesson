# 1 вариант (целое число)

def square(number):
    return number * number
number = int(input("сторона квадрата: "))
x = square(number)


print(x)


# 2 вариант (число с плавающей точкой) округление ответа

import math

def square(number1):
    return number1 * number1

from math import ceil
number1 = float(input("сторона квадрата равна: "))
   
y = ceil(square(number1))


print(y)