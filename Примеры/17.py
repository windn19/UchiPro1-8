import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'

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
