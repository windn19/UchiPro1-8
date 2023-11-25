# 4. Напиши программу, в которой создай класс Date. Реализуй в классе следующие методы:
#     • __init__(d, m, y) — добавляет объекту атрибуты d, m, y — день, месяц и год;
#     • __str__() — возвращает текстовое представление объекта в формате: «d.m.y»;
#     • методы сравнения.
#
# Входные данные:
# Вводится три строки — на первой и второй строке вводятся даты в формате d.m.y, на третьей строке вводится
# одна из операций сравнения ==, !=, >, >=, <, <=.
#
# Выходные данные:
# Выводится True или False — результат сравнения объектов.
#
# Пример ввода:
# 1.1.2000
# 31.12.1999
# >
#
# Пример вывода:
# True

from functools import total_ordering


@total_ordering
class Date:
    def __init__(self, d, m, y):
        self.d, self.m, self.y = d, m, y

    def __eq__(self, other):
        return (self.y, self.m, self.d) == (other.y, other.m, other.d)

    def __lt__(self, other):
        return (self.y, self.m, self.d) < (other.y, other.m, other.d)

    def __str__(self):
        return f'{self.d}.{self.m}{self.y}'


date_1 = Date(*map(int, input().split('.')))
date_2 = Date(*map(int, input().split('.')))
op = input()
if op == '==':
    print(date_1 == date_2)
elif op == '!=':
    print(date_1 != date_2)
elif op == '>':
    print(date_1 > date_2)
elif op == '>=':
    print(date_1 >= date_2)
elif op == '<':
    print(date_1 < date_2)
elif op == '<=':
    print(date_1 <= date_2)

# match op:
#     case '==':
#         print(date_1 == date_2)
#     case '!=':
#         print(date_1 != date_2)
#     case '>':
#         print(date_1 > date_2)
#     case '>=':
#         print(date_1 >= date_2)
#     case '<':
#         print(date_1 < date_2)
#     case '<=':
#         print(date_1 <= date_2)
