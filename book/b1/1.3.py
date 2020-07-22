import cmath

# 1.1 복소수
# z = a + bj

# 파이썬에서 복소수는 한 쌍을 갖는 불변형이다.
# 복소수를 사용하려면 cmath 모듈을 임포트해야 한다.

z = 3 + 2j

# a
print(z.real) # 3.0

# b
print(z.imag) # 2.0

# a - bj
print(z.conjugate()) # 3-2j
