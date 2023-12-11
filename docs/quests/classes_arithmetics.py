# * quests
# - class Arithmetic : 곱셈, 나눗셈 할 수 있는 function 추가
# - 출력 : 뺄셈, 곱셈, 나눗셈 실행

# # class basic format
# class Class_name :
#     def __init__(self) :   
#         pass

#     def function_name(self) :             
#         pass
#         return 0
    

# 사칙연산 되는 class 작성
# 뺄셈, 곱셈, 나눗셈
class Arithmetics:
    def __init__(self) :   # 생성자(class가 갖고 있는 자원) (자원=function)
        pass

    def minus(self, first, second) : 
        result = first - second      # 내용 넣기
        return result
    
    def multiply(self, first, second) :  # self : class의 자원
        sum = first * second
        # return 0
        return sum # 상수(예.0) 대신 변수 사용
    
    def divide(self, first, second) :  # self : class의 자원
        sum = first / second
        # return 0
        return sum # 상수(예.0) 대신 변수 사용

# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
arithmetics = Arithmetics()   # Arithmetics()를 재활용하기 위해 arithmetics라는 변수에담음 / Arithmetics() - 일회성, arithmetics - 재활용성
# 3. call function
print(arithmetics.minus(24, 4))
print(arithmetics.multiply(24, 4))
print(arithmetics.divide(24, 4))
pass