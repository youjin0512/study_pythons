# 기존 문법을 압축된 방식으로 구현 (2가지)
# 1.for, if문(삼항연산자)
# 2.lambda(람다)
lambda param : param + 2      # function없이 선언만 있음
# lambda param : param + 2(param)
def function_name(param):
    pass
    return 0

# 압축된 lambda식 for문 적용
numerics = [0, 1, 2, 3, 4]  # 5(다섯)개수 값으로 이루어진 리스트
print([number+2 for number in numerics])   # list append
pass
print([(lambda param : param + 2)(number) for number in numerics])
pass


# 각 숫자의 제곱을 계산
numbers = [1, 2, 3, 4, 5]  # list
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]