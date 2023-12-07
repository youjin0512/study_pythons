# * quests
# - 사용자 입력 반복 곱셈 계산기
# - 'q' 입력 시 (계산)종료
# - function 2개 사용
#   하나는 return, 하나는 내가 필요에 의해 고민해서 만들면 됨.

#### 기본양식
# def function_name() : 
#   num_first =
#   num_second = 5
#   return 0

def mul(a,b) : 
  return a*b

while True :
    menu = int(input("원하는 계산기 기능을 입력하세요."))
    if(menu <= 5):
        number_a = int(input("첫번째 숫자를 입력하세요."))
        number_b = int(input("두번째 숫자를 입력하세요."))
        if(menu <= 5):
            result = mul(number_a, number_b)
        print("결과는 %d 입니다."%result)
    elif(menu == 6):
        break
    else:
        print("잘못입력하셨습니다. 다시 입력해주세요.")