# 코드 기본 형식
## import 시 주로 사용하는 방식
from classes_formats import Person, Arithmetics, Class_name  # classes_formats : module

# class basic format
class Class_name :
    def __init__(self) :   #생성자 (class의 생성자), class가 갖고 있는 하나의 성격(class 자체가 갖고 있는 function) / class가 갖고 있는 모든 자원을 return해서 return을 쓸(명기할) 필요가 없음
        try:
            pass    # '업무 코드' 입력 부분                                
        except:
            pass    # 업무 코드 문제 발생 시 '대처 코드'
        finally :
            pass    # try나 except이 끝난 후 '무조건 실행 코드'

    def function_name(self) :  # self 키워드 필요(class 소속 확인용) / 'self'는 디폴트 값 -> "나는 이 class에 속한 function이야" --> class에서만 사용되는 키워드
        try:
            pass    # '업무 코드' 입력 부분                                
        except:
            pass    # 업무 코드 문제 발생 시 '대처 코드'
        finally :
            pass    # try나 except이 끝난 후 '무조건 실행 코드'
        return 0

# 기본 function 형식 - 기다림. 불리울 때 기능한다.
def function_name() : 
    try:
        pass    # '업무 코드' 입력 부분                                
    except:
        pass    # 업무 코드 문제 발생 시 '대처 코드'
    finally :
        pass    # try나 except이 끝난 후 '무조건 실행 코드'
    return 0

if __name__ == "__main__" :
    pass
    try:
        pass    # '업무 코드' 입력 부분                                
    except:
        pass    # 업무 코드 문제 발생 시 '대처 코드'
    finally :
        pass    # try나 except이 끝난 후 '무조건 실행 코드'
