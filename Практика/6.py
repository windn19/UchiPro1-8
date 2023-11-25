class Brick():
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def __add__(self, other):
        if (self.l, self.w) == (other.l, other.w):
            return Brick(self.l, self.w, self.h + other.h)
        elif (self.w, self.h) == (other.w, other.h):
            return Brick(self.l + other.l, self.w, self.h)
        elif (self.l, self.h) == (other.l, other.h):
            return Brick(self.l, self.w + other.w, self.h)
        else:
            return Brick(min(self.l, other.l), min(self.w, other.w), min(self.h, other.h))

    def __mul__(self, other):
        if isinstance(other, int):
            return Brick(self.l * other, self.w, self.h)

    def __str__(self):
        return f'Brick({self.l}, {self.w}, {self.h})'

print(eval(input()))