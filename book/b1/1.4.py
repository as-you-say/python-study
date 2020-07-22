from fractions import Fraction

# 1.4 fraction 모듈
# 분수를 다루는 경우에 사용합니다.

def float_to_fractions(number):
    """ 분수를 반환한다 """
    return Fraction(*number.as_integer_ratio())

def get_denominagor(number1, number2):
    """ 분모를 반환한다 """
    a = Fraction(number1, number2)
    return a.denominator

def get_numerator(number1, number2):
    """ 분모를 반환한다 """
    a = Fraction(number1, number2)
    return a.numerator

print(float_to_fractions(1.25))
print(get_denominagor(5, 4))
print(get_numerator(5, 4))
