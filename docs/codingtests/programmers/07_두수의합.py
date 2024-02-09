# Description
# 정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.

# 제한사항
# -50,000 ≤ num1 ≤ 50,000
# -50,000 ≤ num2 ≤ 50,000

# 입출력 예
# num1	num2	result
# 2	3	5
# 100	2	102

# 입출력 예 설명
# 입출력 예 #1
# num1이 2이고 num2가 3이므로 2 + 3 = 5를 return합니다.

# 입출력 예 #2
# num1이 100이고 num2가 2이므로 100 + 2 = 102를 return합니다.

num1, num2 = input().split()                    # 문자로 입력을 받고
pass
num1 = int(num1)                        # 입력 받은 문자를 숫자로 변환
num2 = int(num2)                        # 입력 받은 문자를 숫자로 변환
def solution(num1, num2):
    answer = num1 + num2
    return answer
answer = solution(num1, num2)
print(answer)
pass