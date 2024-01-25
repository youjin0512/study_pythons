# 사칙연산

# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)     # // : 소숫점 제거
print(a % b)

# 제출하기 전에 예제 출력해보기(Run, F5)