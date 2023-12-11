# class 사용 순서
# 1. import : 같은 파일에 있을 경우 생략  #지정
# 2. class instance : 생성자 호출               #class 대기(stand-by)
# 3. call function : 원하는 기능 호출

# class basic format
class Class_name :
    def __init__(self) :   #생성자 (class의 생성자), class가 갖고 있는 하나의 성격(class 자체가 갖고 있는 function) / class가 갖고 있는 모든 자원을 return해서 return을 쓸(명기할) 필요가 없음
        pass

    def function_name(self) :                # self 키워드 필요(class 소속 확인용) / 'self'는 디폴트 값 -> "나는 이 class에 속한 function이야" --> class에서만 사용되는 키워드
        pass
        return 0
    
class Person :
    def add_age(self) :                      # self를 넣어줘야지만 동작이됨
        pass
        print("45세")
        return 0
    
# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance화 : class의 이름을 부르는것
person = Person() # 변수(person)의 성격에 class가 담김  # Person() : class를 부르기 위한 하나의 방법, 실제로는 동작하지 않고 묶어놓기만 하는것. fuction을 통해서만 동작.
# 3. call function
person.add_age()


# 사칙연산 되는 class 작성  ;  한 클래스내에 묶어서 덧셈,뺄셈 넣기 (사칙연산 class 만들기)
# 덧셈, 뺄셈
class Arithmetics:
    def __init__(self) :   # 생성자(class가 갖고 있는 자원) (자원=function)
        pass

    def add(self, first, second) :  # self : class의 자원
        sum = first + second
        # return 0
        return sum # 상수(예.0) 대신 변수 사용

    def minus(self, first, second) : 
        result = first - second      # 내용 넣기
        return result

# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
arithmetics = Arithmetics()   # Arithmetics()를 재활용하기 위해 arithmetics라는 변수에담음 / Arithmetics() - 일회성, arithmetics - 재활용성
# 3. call function
print(arithmetics.add(5, 6))
pass
