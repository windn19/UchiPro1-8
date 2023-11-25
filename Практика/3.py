# 3. Напиши программу, в которой определи методы сравнения в классе Fraction (обыкновенная дробь):
# ==, !=, >, >=, < (уже реализовано), <=. При решении задачи используй готовый код примеров в качестве шаблона.
#
# Считай с клавиатуры две строки, содержащие два целых числа через пробел — числитель и знаменатель первой дроби
# и числитель и знаменатель второй дроби. Создай экземпляры класса Fraction с параметрами, считанными с клавиатуры.
# Выведи результаты операций сравнения этих дробей: ==, !=, >, >=, <, <=.
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
# Пример вывода:
# False
# True
# False
# False
# True
# True

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

    def __eq__(self, other):
        # common_den = self.get_common_denominator(self.den, other.den)
        # return common_den // self.den * self.num == common_den // other.den * other.num
        return self.num * other.den == other.num * self.den

    def __ne__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num != common_den // other.den * other.num

    def __gt__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num > common_den // other.den * other.num

    def __ge__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num >= common_den // other.den * other.num

    def __lt__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num < common_den // other.den * other.num

    def __le__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num <= common_den // other.den * other.num

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'


num, den = map(int, input().split())
fraction1 = Fraction(num, den)
num, den = map(int, input().split())
fraction2 = Fraction(num, den)
print(fraction1 == fraction2)
print(fraction1 != fraction2)
print(fraction1 > fraction2)
print(fraction1 >= fraction2)
print(fraction1 < fraction2)
print(fraction1 <= fraction2)
