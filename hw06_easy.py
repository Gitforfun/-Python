# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    # функция-конструктор - запускается автоматически при создании объекта (экземпляра класса)

    def __init__(self, point_a: tuple, point_b: tuple, point_c: tuple):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    # методы:

    def lines(self):
        a_b = math.sqrt(abs(self.point_a[0] - self.point_b[0]) ** 2 + abs(self.point_a[1] - self.point_b[1]) ** 2)
        b_c = math.sqrt(abs(self.point_b[0] - self.point_c[0]) ** 2 + abs(self.point_b[1] - self.point_c[1]) ** 2)
        c_a = math.sqrt(abs(self.point_c[0] - self.point_a[0]) ** 2 + abs(self.point_c[1] - self.point_a[1]) ** 2)
        return a_b, b_c, c_a

    def perimetr(self):
        perim_triang = 0
        lines_list = self.lines()
        for lin in lines_list:
            perim_triang += lin
        return perim_triang

    def square(self):
        # 1/2 * h_a * b_c
        lines_list = self.lines()
        p = (self.perimetr()) / 2
        h_bc = (2 * math.sqrt(p * (p - lines_list[1]) * (p - lines_list[2]) * (p - lines_list[0]))) / lines_list[1]
        return h_bc * lines_list[1] / 2


treugol_1 = Triangle((1, 1), (3, 5), (0, 7))
print(treugol_1.perimetr())
print(treugol_1.lines())
print(treugol_1.square())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# условия ввода точек: верхнее основание - отрезок BC, нижнее основание - отрезок AD
class Isosceles_trapezoid:
    def __init__(self, point_a: tuple, point_b: tuple, point_c: tuple, point_d: tuple):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def lines(self):
        a_b = math.sqrt(abs(self.point_a[0] - self.point_b[0]) ** 2 + abs(self.point_a[1] - self.point_b[1]) ** 2)
        b_c = math.sqrt(abs(self.point_b[0] - self.point_c[0]) ** 2 + abs(self.point_b[1] - self.point_c[1]) ** 2)
        c_d = math.sqrt(abs(self.point_c[0] - self.point_d[0]) ** 2 + abs(self.point_c[1] - self.point_d[1]) ** 2)
        d_a = math.sqrt(abs(self.point_d[0] - self.point_a[0]) ** 2 + abs(self.point_d[1] - self.point_a[1]) ** 2)
        return a_b, b_c, c_d, d_a

    def tru_trap(self):
        lines_trap = self.lines()
        return lines_trap[0] == lines_trap[2]

    def perimetr(self):
        p_trap = 0
        lines_list = self.lines()
        for lin in lines_list:
            p_trap += lin
        return p_trap

    def square(self):
        lines_trap = self.lines()
        h_trap = math.sqrt(4 * (lines_trap[0] ** 2) - (abs(lines_trap[1] - lines_trap[3])) ** 2) / 2
        square_trap = ((lines_trap[1] + lines_trap[3]) / 2) * h_trap
        return square_trap


new_trap = Isosceles_trapezoid((1, 1), (2, 5), (6, 5), (7, 1))
print(new_trap.tru_trap())
print(new_trap.lines())
print(new_trap.perimetr())
print(new_trap.square())
