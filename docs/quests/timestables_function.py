# # * quests
# # - refer : /docs/quests/timestables.py
# # - [30, 35, 20] 단수 대한 출력
# # - timestables_fors.py -> function 화
# # - option) [30, 35, 20] 부분 사용자 입력, 'q'이면 종료

# #######################################################지수님
# def timestables(x) : # 'x'에 user의 input 받음
#     numbering=[0, 1, 2, 3, 5,  6, 7, 8] # 9단까지만 실행
#     for loop in numbering: # 9단까지 반복 실행
#         print("{}*{}={}".format(x, loop+1, (loop+1)*x)) # 구구단 포맷-출력/계산
#     return stop() # 이후 무조건 stop() 실행시키기 위해 return stop()

# def stop() : # 종료할지 말지 결정하는 function
#     str_input=input("구구단 몇단(종료하려면 q 입력) : ") # 이전 input과 달리 종료 sign을 누를 수 있게 함
#     if str_input !="q" : # user input이 q가 아닐 경우 timetables() 실행 - 안에 필요한 변수 입력함.
#         timestables(int(str_input))
#     else : # q가 나올 경우 종료
#         print("End Program!")

# # 초기 user input
# str_input=input("구구단 몇단 : ")
# # timestables() 실행
# timestables(int(str_input))



def timestables() : # 'x'에 user의 input 받음
    num_put = int(str_put)
    num_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 9단까지만 실행
    if num_put == 30 :
        for x in num_lists :
            print("30*{}={}".format(x, 30*x))
    elif num_put == 35:
        for x in num_lists :
            print("35*{}={}".format(x, 35*x))
    elif num_put == 20:
        for x in num_lists :
            print("20*{}={}".format(x, 20*x))
    else :
        print("입력할 수 없는 숫자입니다.")

    return stop() # 이후 무조건 stop() 실행시키기 위해 return stop()

def stop() : # 종료할지 말지 결정하는 function
    str_input=input("구구단 몇단(종료하려면 q 입력) : ") # 이전 input과 달리 종료 sign을 누를 수 있게 함
    if str_input !="q" : # user input이 q가 아닐 경우 timetables() 실행 - 안에 필요한 변수 입력함.
        timestables()
    else : # q가 나올 경우 종료
        print("End Program!")

# 초기 user input
str_put = input("구구단 몇단(종료하려면 q 입력) : ")
# timestables() 실행
timestables()


# num_put = int(input())
# num_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num_put in num_lists:
#     print("30*{}={}".format(num_put, 30*num_put))

# for num_put in num_lists:
#     print("35*{}={}".format(num_put, 35*num_put))

# for num_put in num_lists:
#     print("20*{}={}".format(num_put, 20*num_put))

# str_thirty = "30단"
# str_thirty_five = "35단"
# str_twenty = "20단"
# def mul_tables() : 
#       pint(str_thirty)
#       print("30*{}={}".format(num_put, 30*num_put))
#       return str_thirty
