import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        # common_den = self.get_common_denominator(self.den, other.den)
        # num = common_den // self.den * self.num + common_den // other.den * other.num
        # num, den = self.get_reduced_fraction(num, common_den)
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __iadd__(self, other):
        # common_den = self.get_common_denominator(self.den, other.den)
        # num = common_den // self.den * self.num + common_den // other.den * other.num
        # self.num, self.den = self.get_reduced_fraction(num, common_den)
        return self + other

    def __radd__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self + other

    @staticmethod
    def get_reduced_fraction(num, den):
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den


fraction_1 = Fraction(1, 2)
fraction_2 = Fraction(3, 9)
fraction_3 = fraction_1 + fraction_2
print(fraction_3)
print(2 + fraction_3)
print(fraction_3 + 2)
fraction_1 += Fraction(1, 2)
print(fraction_1)
