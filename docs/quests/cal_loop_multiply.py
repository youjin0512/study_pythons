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


# # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def multiply_repeat(num_1, num_2) :
#     result = num_1 * num_2
#     return result
    
# def end_program() :
#     result = "프로그램을 종료합니다."
#     return result

# while True :
#     input_data = input()
#     if "q" in input_data:
#         print(end_program())
#         break
#     else :
#         input_data_1, input_data_2 = map(int, input_data.split())
#         print(multiply_repeat(input_data_1, input_data_2))
#         pass

# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# num_statistics = [0, 0]
# num_first = int(num_statistics+1)
# num_second = num_statistics
# def infinite_number() : 
#   my_score = 85
#   calculator = ''
#   if my_score >= 90 : # 90점 이상 : A,
#     calculator = 'A'
#   elif my_score > 80 : # 80점 초과 : B
#     calculator = 'B'
#   else :               # 나머지 : F
#     calculator = 'F'
#   # return_listbyindex() # function 내에서도 fuction 작성 가능
#   return calculator

# str_grade = return_grade()

# print("{} * {} = {}".format((num_statistics+1,), num_statistics),((num_statistics+1)*num_statistics))


# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def multiply() : 
#   num_first = 4
#   num_second = 5
#   # 곱셈 연산
#   result = num_first * num_second
#   return result

# ##결과값 20 불러내기
# # 방법 3.
# num_multiply = multiply()
# print("num_multiply() return value : {}".format(num_multiply))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##if문 바꾸는 방법
# my_score = 79
# if my_score >= 90 : # 90점 이상 : A,
#     print("{}은 90점 이상으로 A학점.".format(my_score))
# elif my_score > 80 : # 80점 초과 : B
#     print("{}은 80점 초과로 B학점.".format(my_score))
# else :               # 나머지 : F
#     print("{}은 80점 이하이므로 F학점.".format(my_score))
# 반복 print 작업을 줄이기 위한 function 만들기
