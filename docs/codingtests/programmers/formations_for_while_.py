# Description
## 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.

# 제한사항
## 0 < age ≤ 120
## 나이는 태어난 연도에 1살이며 1년마다 1씩 증가합니다.

# 입출력 예
## age	result
## 40	1983
## 23	2000

# 입출력 예 설명
## 입출력 예 #1
# 2022년 기준 40살이므로 1983년생입니다.

# 입출력 예 #2
## 2022년 기준 23살이므로 2000년생입니다.

# age = int(input())
# # dateofbirth = 2023 - age
# # print(dateofbirth)
# def solution(age):
#     answer = 2023 - age
#     return answer
    
# dateofbirth = solution(age)
# print(dateofbirth)
# pass

def solution(age):
    answer = 2023 - age
    return answer

# for문 연습
for i in range(4):
    age = int(input())    
    dateofbirth = solution(age)
    print(dateofbirth)
    pass

# while문 연습
while True:
    age = int(input()) 
    if age == 0:
        break   
    else:
        dateofbirth = solution(age)
        print(dateofbirth)
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