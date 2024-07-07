import math

class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __mul__(self, b):
        result_num = self.numerator * b.numerator
        result_den = self.denominator * b.denominator
        return Fraction(result_num, result_den)

    def __truediv__(self, b):
        result_num = self.numerator * b.denominator
        result_den = self.denominator * b.numerator
        return Fraction(result_num, result_den)

    def __add__(self, b):
        result_num = (self.numerator * b.denominator) + (self.denominator + b.numerator)
        result_den = self.denominator * b.denominator
        return Fraction(result_num, result_den)

    def __sub__(self, b):
        result_num = (self.numerator * b.denominator) - (self.denominator + b.numerator)
        result_den = self.denominator * b.denominator
        return Fraction(result_num, result_den)
    
    def __pow__(self, n):
        result_den = self.numerator ** n
        result_num = self.denominator ** n
        return Fraction(result_num, result_den)

    def simplify(self):
        common_divisor = math.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // common_divisor, self.denominator // common_divisor)


# Use example:

fract1 = Fraction(2,4)
fract2 = Fraction(5,10)

result = fract1 + fract2

print(f'The result of {fract1} + {fract2} is: {result}')

