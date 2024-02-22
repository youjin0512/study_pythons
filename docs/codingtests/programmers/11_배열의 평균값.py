# Description
## 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

# 제한사항
## 0 ≤ numbers의 원소 ≤ 1,000
## 1 ≤ numbers의 길이 ≤ 100
## 정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.

# 입출력 예
## numbers	result
## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	5.5
## [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]	94.0

# 입출력 예 설명
## 입출력 예 #1
## numbers의 원소들의 평균 값은 5.5입니다.

## 입출력 예 #2
## numbers의 원소들의 평균 값은 94.0입니다.

### 1) 전체합산
### 2) 전체합산 / n개

numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# 방법1)
def solution(numbers):
    i = 0
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    divide = sum / len(numbers)
    return divide
average = solution(numbers)
print(average)
pass
# 방법2)
def solution(numbers):
    Sum = sum(numbers)
    divide = Sum / len(numbers)
    return divide
print(solution(numbers))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def solution(numbers):
#     i = 0
#     sum = 0
#     for i in range(10):
#         j = i + 1
#         sum = sum + j
#     divide = sum / len(numbers)
#     return divide
# average = solution(numbers)
# print(average)