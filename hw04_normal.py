# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

print(re.findall(r'[a-z]{1,}', line))
print(' ниже без Re. Решение подсмотрено. Разобрал по-этапно с комментариями. Для понимания и запоминания.')
capital_letters = list(map(lambda letter: chr(letter), list(range(65, 91))))  # генерируем список заглавных букв
#print(capital_letters)
new_line = list(line)  # переводим текст в список по буквам
#print(new_line)
for i, all_letter in enumerate(new_line[:]):  # для каждого пронумерованного элемента из побуквенного списка:
       for capital_letter in capital_letters:  # перечисляем все заглавные буквы:
              if all_letter is capital_letter:  # если текущая буква из общего списка является заглавной
                     new_line[i] = ' '  # заменяем эту заглавную букву на пробел
#print(new_line)
string_line = ''  # создаем чистую стоку. Всё можно написать коротко. Но расписываю по-этапно, дабы лучше понять
string_line = string_line.join(new_line)  # склеиваем в строку
#print(string_line)
string_line = string_line.split(' ')  # создаем список с разделением по пробелу
#print(string_line)
string_line_list = [i for i in string_line if i is not '']  # ген-ем новый список на основе string_line но без пустот
print(string_line_list)
print()
# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

print(re.findall(r"[a-z]{2}([A-Z]{1,})[A-Z]{2}", line_2))

print('Ниже вариант без Re')
capital_letters = list(map(lambda letter: chr(letter), list(range(65, 91))))  # генерируем список заглавных букв
lower_letters = list(map(lambda letter: chr(letter), list(range(97, 123))))  # генерируем список заглавных букв
#print(capital_letters)
#print(lower_letters)
new_line = list(line_2)  # Переводим каждый символ в элемент списка

list_search = []  # создаем пустой список, чтобы в дальнейшем его заполнять найденными значениями
i = len(new_line) - 1  # находим максимальный индекст списка. Т.к. начинается с 0, вычитаем единицу

while i >= 0:
       if new_line[i] in lower_letters:  #  если в общем списке есть буквы нижнего регистра
              list_search.append(new_line[i])  # добавляем в новый список
       elif new_line[i] in capital_letters and i <= len(new_line) -3 and new_line[i+1] in capital_letters and new_line[i+2] in capital_letters:
              list_search.append(new_line[i])  # добавляем в новый список если заглавная и последующие 2 тоже заглавные
       else:
              list_search.append(' ')  # если выше условия не удовлетворяют, записываем пробел в новый список
       i -= 1
list_search.reverse()  # реверс списка
#print(list_search)

i = 0
list_search2 = []
flag = True  # первоначальные условия поиска сортировки символов в верхнем регистре
# Фильтрация
while i <= len(list_search) - 1:
       if list_search[i] in lower_letters:
              flag = True
       if list_search[i] in capital_letters and list_search[i - 1] in lower_letters and list_search[i - 2] in lower_letters:
              list_search2.append(list_search[i])
              flag = False
       elif list_search[i] in capital_letters and flag is False:
              list_search2.append(list_search[i])
       else:
              list_search2.append(' ')
       i += 1
#print(list_search2)

my_line = ''.join(list_search2).split(' ')

exit_line = [i for i in my_line if i != '']
print(exit_line)
print()

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

# -*- coding: utf-8 -*-
import random
#import os
import itertools

file_name = input('Введите имя файла (без расширения, будет txt): ')
file_name = file_name + '.txt'
#print(os.path.join('D:', 'PycharmProjects', 'python_basic_hw'))
#print(file_name)

my_file = open(file_name, 'w')

my_range = 2500

digital_list = [random.randint(0, 9) for digit in range(my_range)]
#print(digital_list)
#print(list(map(lambda x: str(x), digital_list)))
digital_list = ''.join(list(map(lambda x: str(x), digital_list)))

print(digital_list)
#print('длина строки: ', len(digital_list))

my_file.write(digital_list)
my_file.close()

my_file = open(file_name, 'r')
second_dig_list = my_file.read()
my_file.close()

#print(second_dig_list)
print(max((list(g) for k, g in itertools.groupby(second_dig_list)), key = len))




