# 1.  Напиши программу, в которой определи методы арифметических операций в классе Fraction (обыкновенная дробь):
# сложение (уже реализовано), вычитание, умножение и деление. При решении задачи используй готовый код
# примеров в качестве шаблона.
#
# Считай с клавиатуры две строки, содержащие два целых числа через пробел — числитель и знаменатель первой дроби
# и числитель и знаменатель второй дроби. Создай экземпляры класса Fraction с параметрами, считанными с клавиатуры.
# Выведи результаты арифметических операций: сложение, вычитание, умножение, деление (/) этих дробей.
#
# Входные данные:
# Вводится две строки, каждая строка содержит два целых числа через пробел — числитель и знаменатель первой дроби
# и числитель и знаменатель второй дроби.
#
# Выходные данные:
# Выводится 4 строки в формате «Дробь {числитель}/{знаменатель}».
#
# Пример ввода:
# 1 2
# 2 3
#
# Пример вывода:
# Дробь 7/6
# Дробь -1/6
# Дробь 1/3
# Дробь 3/4

import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    @staticmethod
    def get_reduced_fraction(num, den):
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den

    def __add__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        num = common_den // self.den * self.num + common_den // other.den * other.num
        num, den = self.get_reduced_fraction(num, common_den)
        return Fraction(num, den)

    def __sub__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        num = common_den // self.den * self.num - common_den // other.den * other.num
        num, den = self.get_reduced_fraction(num, common_den)
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        num, den = self.get_reduced_fraction(num, den)
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        num, den = self.get_reduced_fraction(num, den)
        return Fraction(num, den)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'


num, den = map(int, input().split())
fraction1 = Fraction(num, den)
num, den = map(int, input().split())
fraction2 = Fraction(num, den)
print(fraction1 + fraction2)
print(fraction1 - fraction2)
print(fraction1 * fraction2)
print(fraction1 / fraction2)
