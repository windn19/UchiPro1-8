class Test:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return 'Вызов метода __add__'

    def __radd__(self, other):
        return 'Вызов метода __radd__'

    def __iadd__(self, other):
        self.x = self.x + other
        return self

    def __str__(self):
        return f'x = {self.x}'


a = Test(1)
print(a + 2)  # Вызов метода __add__
print(2 + a)  # Вызов метода __radd__
a += 2
print(a)  # x = 3
