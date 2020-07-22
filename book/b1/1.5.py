from decimal import Decimal

# 1.5 decimal 모듈
# 정확한 10진법의 부동소수점 숫자가 필요한 경우에 사용.
# 부동 소수점 불변 타입인 decimal.Decimal을 사용할 수 있다.
# 정수 또는 문자열을 인수로 취한다 - 파이썬 3.1부터 사용할 수 있다.


# sum(a for i in range(n))
# a 라는 수를 n 번 곱하기
print(sum(Decimal(0.1) for i in range(10)))


# 10진수 비교
print(sum(Decimal(0.1) for i in range(10)))
print(Decimal("1.0"))
print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))

