from math import sqrt

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c): 
        if isinstance(c, Complex): return Complex(self.r + c.r, self.i + c.i)
        else: return Complex(self.r + c, self.i)

    def __sub__(self, c): 
        if isinstance(c, Complex): return Complex(self.r - c.r, self.i - c.i)
        else: return Complex(self.r - c, self.i)

    def __mul__(self, c):
        if isinstance(c, Complex): 
            return Complex( (self.r*c.r - self.i*c.i), (self.r*c.i + self.i*c.r))
        else: 
            return Complex(c * self.r, c * self.i)

    def __truediv__(self, c): 
        return Complex(0, 0)  

    def __abs__(self):
        return sqrt(self.r**2 + self.i**2)

    def __neg__(self):
        return Complex(-self.r, -self.i)

    def __eq__(self, c):
        if isinstance(c, Complex): return self.r == c.r and self.i == c.i
        else: return self.r == c.r

    def __ne__(self, c):
        return not self.__eq__(c)

    def __str__(self):
        if self.i > 0:
            return '{} + i{}'.format(self.r, self.i)
        elif self.i == 0:
            return '{}'.format(self.r)
        else:
            return '{} - i{}'.format(self.r, abs(self.i))

    def __repr__(self):
        return 'Complex: {}'.format(self.__str__())


if __name__ == '__main__':
    c1 = Complex(1, -1)
    c2 = Complex(-1, 1)
    print('c1: ', c1)
    print('c2: ', c2)
    print('c1 + c2: ', c1 + c2)
    print('c1 + 6: ', c1 + 6)
    print('c1 - c2: ', c1 - c2)
    print('c2 - 6: ', c2 - 6)
    print('c1 * c2: ', c1 * c2)
    print('c1 / c2: ', c1 / c2)
    print('-c1: ', -c1)
    print('c1 == c2: ', c1 == c2)
    print('not c1: ', not c1)
