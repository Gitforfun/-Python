import os  # Импортируем всю библиотеку.
# path mkdir  # тут указываю все используемые функции, чтобы потом оптимизировать


def make_dir(dir_name):  # Функция создания директрорий dir_1 - dir_9
    dir_path = os.path.join(os.getcwd(), dir_name)  # полный адрес запускаемого скрипта + название новой директории
    try:
        os.mkdir(dir_path)  # пробуем создать папку
        print(f'Создана директрория {dir_name}')
    except FileExistsError:  # если папка уже есть и возникает ошибка FileExistsError, продолжаем выполнять скрипт
        print(f'Директрория {dir_name} уже существует')


def del_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)  # полный адрес запускаемого скрипта + название новой директории
    if os.path.isdir(dir_path):
        os.removedirs(dir_path)
        print(f'Директрория {dir_name} и всё содержимое удалены.')
    else:
        print(f'Директрория {dir_name} не существует.')


def goto_dir(dir_name):
    try:
        os.chdir(dir_name)
        print(f'Успешно перешли в директорию {dir_name}')
        print('Ваше расположение: ', os.getcwd())
    except FileNotFoundError:
        print(f'Директрории {dir_name} не существует')


# для тестирования
if __name__ == '__main__':
    print('Проверка тестирования')
    print(os.getcwd())
    goto_dir('dir_1')
    goto_dir('dir_1')
    goto_dir('..')

