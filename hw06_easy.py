# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    # функция-конструктор - запускается автоматически при создании объекта (экземпляра класса)
    def __init__(self, point_a: tuple, point_b: tuple, point_c: tuple):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def lines(self):
        a_b = math.sqrt(abs(self.point_a[0] - self.point_b[0]) ** 2 + abs(self.point_a[1] - self.point_b[1]) ** 2)
        b_c = math.sqrt(abs(self.point_b[0] - self.point_c[0]) ** 2 + abs(self.point_b[1] - self.point_c[1]) ** 2)
        c_a = math.sqrt(abs(self.point_c[0] - self.point_a[0]) ** 2 + abs(self.point_c[1] - self.point_a[1]) ** 2)
        return a_b, b_c, c_a

    def perimetr(self):
        perimetr = 0
        lines_list = self.lines()
        for lin in lines_list:
            perimetr = perimetr + lin
        return perimetr

    def square(self):
        # 1/2 * h_a * b_c
        lines_list = self.lines()
        p = (self.perimetr())/2
        h_bc = (2 * math.sqrt(p * (p - lines_list[1])*(p - lines_list[2])*(p - lines_list[0])))/ lines_list[1]
        return h_bc * lines_list[1] / 2


treugol_1 = Triangle((1, 1), (3, 5), (0, 7))
print(treugol_1.perimetr())
print(treugol_1.lines())
print(treugol_1.square())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# условия ввода точек: верхнее основание - отрезок BC, нижнее основание - отрезок AC
class Isosceles_trapezoid:
    def __init__(self, point_a: tuple, point_b: tuple, point_c: tuple, point_d: tuple):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

        print()