# 1.7 연습문제


# 1.7.1 진법 변환
# 2 <= base <= 10
# 몰풀었습니다 ㅠ

# 문제 : 10진법을 base 진법으로 고치기
# 몫을 10으로 나눈다
# 나머지를 순서대로 base의 0제곱 1제곱 2제곱 .... 을 하여 더한다
def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result

# 문제 : base 진법을 10진법으로 고치기
# 몫을 base로 나눈다
# 나머지를 순서대로 10의 0제곱 1제곱 2제곱 .... 을 하여 더한다
def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number = number // base

# 문제 : 10진법을 base 진법으로 고치기 (16진수까지)
# - 재귀합수 미사용
def convert_from_decimal_lager_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    return result
# - 재귀합수 사용
def convert_from_decimal_lager_bases_rec(number, base):
    strings = "0123456789ABCDEFGHIJ"
    if number < base:
        return strings[number]
    else:
        return convert_from_decimal_lager_bases_rec(number // base, base) + strings[number % base]

# 추가학습 : base 진법을 10진법으로 고치기 (16진수까지)
def convert_to_decimal_lager_bases(number, base):
    numberString = str(number)
    strings = "0123456789ABCDEFGHIJ"
    result = 0
    size = len(numberString)
    for i in range(size):
        print(strings.index(numberString[i]))
        print(pow(base, size-i-1))
        result += strings.index(numberString[i]) * pow(base, size-i-1)
    return result






