# 2. Напиши программу, в которой создай класс Time. Реализуй в классе следующие методы:
#     • __init__(h, m) — добавляет объекту атрибуты h и m — часы и минуты;
#     • __str__() — возвращает текстовое представление объекта в формате: «h:m».
# Определи методы арифметических операций:
#     • сложение self + other — возвращает новый объект класса Time;
#     • вычитание self - other — возвращает новый объект класса Time. Если разность будет отрицательной,
#     то разность считать равной 0 (h и m равны 0);
#     • умножение на число self * n — возвращает новый объект класса Time;
# Считай с клавиатуры строку и выведи соответствующий результат:
#     • «h1 m1 + h2 m2» — вывести Time(h1, m1) + Time(h2, m2);
#     • «h1 m1 - h2 m2» — вывести Time(h1, m1) - Time(h2, m2);
#     • «h1 m1 * n» — вывести Time(h1, m1) * n (умножаются и часы и минуты).
#
# Входные данные:
# Вводится строка в формате «h1 m1 + h2 m2», «h1 m1 - h2 m2» или «h1 m1 * n».
#
# Выходные данные:
# Выводится текстовое представление объекта Time, полученного в результате выполнения соответствующей операции.
#
# Пример ввода 1:
# 2 30 + 3 45
# Пример вывода 1:
# 6:15
#
# Пример ввода 2:
# 1 58 - 0 59
# Пример вывода 2:
# 0:59

class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def __str__(self):
        return f'{self.h}:{self.m}'

    def __add__(self, other):
        h, m = divmod(self.h * 60 + self.m + other.h * 60 + other.m, 60)
        return Time(h, m)

    def __sub__(self, other):
        if self.h * 60 + self.m - other.h * 60 + other.m < 0:
            return Time(0, 0)
        h, m = divmod(self.h * 60 + self.m - other.h * 60 - other.m, 60)
        return Time(h, m)

    def __mul__(self, other):
        h, m = divmod((self.h * 60 + self.m) * other, 60)
        return Time(h, m)


s = input().split()
if s[2] == '+':
    print(Time(int(s[0]), int(s[1])) + Time(int(s[3]), int(s[4])))
elif s[2] == '-':
    print(Time(int(s[0]), int(s[1])) - Time(int(s[3]), int(s[4])))
elif s[2] == '*':
    print(Time(int(s[0]), int(s[1])) * int(s[3]))

match s[2]:
    case '+':
        print(Time(int(s[0]), int(s[1])) + Time(int(s[3]), int(s[4])))
    case '-':
        print(Time(int(s[0]), int(s[1])) - Time(int(s[3]), int(s[4])))
    case '*':
        print(Time(int(s[0]), int(s[1])) * int(s[3]))
    case _:
        print('Неизвестная операция')
