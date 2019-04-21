# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class People:  # Создаем базовый класс Люди. Переменные - ФИО. Методы - строки Ф+И+О и краткое Ф+И+О
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    def get_short_name(self):
        return f'{self.surname.title()} {self.name[0].upper()}.{self.patronymic[0].upper()}.'


class Student(People):  # Создаем зависимый класс Учащиеся. Наследование - Люди.
    def __init__(self, name, patronymic, surname, mom, dad, school_class):  # Указываем все переменные
        People.__init__(self, name, patronymic, surname)  # делаем ссылку на переменные базового класса
        self.mom = mom  # Т.е. Люди + мама + папа + учебный класс
        self.dad = dad
        self.school_class = school_class


class Teacher(People):  # Создаем зависимый класс. Базовый - Люди.
    def __init__(self, name, patronymic, surname, subject):  # Указываем все переменные
        People.__init__(self, name, patronymic, surname)  # делаем ссылку на переменные базового класса
        self.subject = subject  # Т.е. Учителя - версия Люди + предмет


class Class_rooms:  # создаем класс Классные комнаты. Класс базовый.
    def __init__(self, class_room, teachers):  # переменные: обозначение класса + лист из преподающих там учителей
        self.class_room = class_room           # прежде чем использовать класс, необходимо создать список учителей.
        self.teachersdict = {t.subject: t for t in teachers}  # при этом список должен составляться исп. класс учителей.


if __name__ == '__main__':
    teachers = [Teacher('Иван', 'Иванович', 'Иванов', 'Труд'),
                Teacher('Петр', 'Петрович', 'Петров', 'Русский язык'),
                Teacher('Сидор', 'Сидорович', 'Сидоров', 'Геометрия'),
                Teacher('Cергей', 'Сергеевич', 'Сергеев', 'Физкультура')]
    classes = [Class_rooms('5 А', [teachers[0], teachers[1]]),
               Class_rooms('5 Б', [teachers[1], teachers[2]]),
               Class_rooms('5 B', [teachers[2], teachers[3]])]
    parents = [People('Семен', 'Семенович', 'Семенов'),
               People('Светлана', 'Васильевна', 'Семенова'),
               People('Роман', 'Романович', 'Романов'),
               People('Руслана', 'Романовна', 'Романова')]
    students = [Student('Игорь', 'Cеменович', 'Семенов', parents[0], parents[1], classes[0]),
                Student('Ольга', 'Романова', 'Романова', parents[2], parents[3], classes[1])]

    print('Список классов в школе: ')
    for i in classes:
        print(i.class_room)

    for i in classes:
        print(f'Учителя, преподающие в {i.class_room} классе:')
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for i in classes:
        print(f"Ученики в классе {i.class_room}:")
        for st in students:
            print(st.get_short_name())
