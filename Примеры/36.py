import math


class Fraction:
    def __init__(self, num, den):
        self.num, self.den = self.get_reduced_fraction(num, den)

    def __str__(self):
        return f'Дробь {self.num}/{self.den}'

    def __getitem__(self, item):
        if item == 0:
            return self.num
        elif item == 1:
            return self.den
        return None

    @staticmethod
    def get_reduced_fraction(num, den):
        gcd = math.gcd(num, den)
        return num // gcd, den // gcd

    @staticmethod
    def get_common_denominator(den1, den2):
        common_den = den1 * den2 // math.gcd(den1, den2)
        return common_den


fraction = Fraction(1, 2)
print(fraction[0])  # 1
print(fraction[1])  # 2
print(fraction[2])  # None
