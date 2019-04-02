__author__ = 'Горбов Андрей Александрович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number = int(input('Task 1. Uses "while". input number: '))
n = 0
digit = 0
digit_max = 0
while n < len(str(number)):
    digit_last = digit
    digit = (number % (10 ** (n + 1))) // (10 ** n)
    if digit_last > digit and digit_max < digit_last:
        digit_max = digit_last
    elif digit_last < digit and digit_max < digit:
        digit_max = digit
    n += 1
print(digit_max)
       
number = input('Task 1.2. Uses "for". input number: ')
digit_last = 0
digit_max = 0
for digit in number:
    digit = int(digit)
    if digit_last > digit and digit_max < digit_last:
        digit_max = digit_last
    elif digit_last < digit and digit_max < digit:
        digit_max = digit
    digit_last = digit
print(digit_max)
    
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input('input "a": '))
b = int(input('input "b": '))

a = a + b
b = a - b
a = a - b

print ('reverce variables: "a" = ', a, ', "b" = ', b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
 
print('input the coefficients "a", "b" and "c": (a*(x^2) + b*x + c = 0):')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
 
discr = b ** 2 - 4 * a * c
print('discriminant = ', discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print('x1 = ', x1) #x1 = %.2f \nx2 = %.2f" % (x1, x2)
    print('x2 = ', x2)
elif discr == 0:
    x = -b / (2 * a)
    print('x = ', x)
else:
    print('no root')
