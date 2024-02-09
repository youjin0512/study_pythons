# Description
## 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.

# 제한사항
## 0 < num1 ≤ 100
## 0 < num2 ≤ 100

# 입출력 예
## num1	num2	result
## 3	2	1500
## 7	3	2333
## 1	16	62

# 입출력 예 설명
## 입출력 예 #1
## num1이 3, num2가 2이므로 3 / 2 = 1.5에 1,000을 곱하면 1500이 됩니다.

## 입출력 예 #2
## num1이 7, num2가 3이므로 7 / 3 = 2.33333...에 1,000을 곱하면 2333.3333.... 이 되며, 정수 부분은 2333입니다.

## 입출력 예 #3
## num1이 1, num2가 16이므로 1 / 16 = 0.0625에 1,000을 곱하면 62.5가 되며, 정수 부분은 62입니다.


## 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후
# 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
num1 = int(input())
num2 = int(input())

def solution(num1, num2):
    division = num1 / num2   # 나누기
    multiplication = int(division * 1000)   # 1000 곱한거에 정수 부분만 가져오기
    answer = multiplication
    return answer
answer = solution(num1, num2)
print(answer)
pass

###############################################
# 1. 입력을 몇 개 어떻게 할 것인가(input)
# 2. 입력한 값들을 어떻게 사용해서 결과값을 만들 것인가
# (non-function 하고 나중에 function에 적용하기)
# - 결과값(answer)을 꼭 만들기
# 3. 출력할 때 변수에 담아서 출력하기 (print(answer))
# 주의사항
# - 모든 줄에 breakpoint 걸어서 어떻게 동작하는지 확인하기.
# - 터미널에는 출력되는 값을 확인할 때 사용
# - debugging에서는 breaking point가 걸려있을 때 변수에 대한 정보(변수에 들어 있는 값, 변수의 타입)를 볼 때 사용