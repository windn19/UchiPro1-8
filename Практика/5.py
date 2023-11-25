# 5. Напиши программу, в которой создай класс Vector (вектор на плоскости). Реализуй в классе следующие методы:
#     • __init__(x, y) — добавляет объекту атрибуты x и y — координаты вектора;
#     • __str__() — возвращает текстовое представление объекта в формате: «Вектор (x, y)»;
#     • __len__() — возвращает длину вектора sqrt(x ** 2 + y ** 2);
#     • методы сравнения — сравниваются длины векторов.
#     • сложение self + other — возвращает новый объект Vector(x1 + x2, y1 + y2);
#     • вычитание self - other — возвращает новый объект Vector(x1 - x2, y1 - y2);
#     • умножение на число self * n — возвращает новый объект Vector(x * n, y* n).
#
# Для того, чтобы сдать данную задачу в тестирующую систему, используй код print(eval(input())).
#
# Входные данные:
# Вводится строка.
#
# Выходные данные:
# Выводится строка.
#
# Пример ввода:
# Vector(2, 0.5) * 2 + Vector(0.5, 3) * 3
# Пример вывода:
# Вектор (5.5, 10.0)

import math
from functools import total_ordering


@total_ordering
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def len_(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.len_() == other.len_()

    def __lt__(self, other):
        return self.len_() < other.len_()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __str__(self):
        return f'Вектор ({self.x}, {self.y})'


print(eval(input()))
