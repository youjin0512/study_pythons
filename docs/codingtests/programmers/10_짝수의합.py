# Description
## 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
## 0 < n ≤ 1000

# 입출력 예
## n	result
## 10	30
## 4	6

# 입출력 예 설명
## 입출력 예 #1
## n이 10이므로 2 + 4 + 6 + 8 + 10 = 30을 return 합니다.

## 입출력 예 #2
## n이 4이므로 2 + 4 = 6을 return 합니다.

number = int(input())

def solution(n): 
    answer = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += i        
    return answer

answer = solution(number)
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
###############################################