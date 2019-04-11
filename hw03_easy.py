# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    from_point = str(number).find('.')  # ищем начало дробной части. Ориентир - точка
    to_compare = int(str(number)[(ndigits + from_point + 1): (ndigits + from_point + 2)])  # первая отсекаемая цифра
    if to_compare >= 5:
        number = number + 0.1 ** ndigits  # если она больше 5, увеличиваем округляемое число
    number = float(str(number)[:(ndigits + from_point + 1)])  # отсекаем лишнее
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)  # переводим в строку
    if len(ticket_number) != 6:  # проверка на шестизаначность
        return 'Некорректный ввод номера билета'
    first_part = ticket_number[:3]  # делаем два среза по 3 цифры
    secont_part = ticket_number[3:]
    return 'Билет счастливый' if sum(map(int, first_part)) == sum(map(int, secont_part)) else 'Обычный билет'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
