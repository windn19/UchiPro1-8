import math
from functools import total_ordering


@total_ordering
class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'

    def __eq__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num == common_den // other.den * other.num

    def __lt__(self, other):
        common_den = self.get_common_denominator(self.den, other.den)
        return common_den // self.den * self.num < common_den // other.den * other.num

    @staticmethod
    def get_reduced_fraction(num, den):
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den


fraction_1 = Fraction(1, 2)
fraction_2 = Fraction(2, 3)
print(fraction_1 == fraction_2)  # False
print(fraction_1 != fraction_2)  # True
print(fraction_1 > fraction_2)  # False
print(fraction_1 >= fraction_2)  # False
print(fraction_1 < fraction_2)  # True
print(fraction_1 <= fraction_2)  # True