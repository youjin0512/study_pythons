# 얼마만큼 반복할지에 대한 '값들'을 알려줌
numeric = 0
numerics = [0, 1, 2, 3, 4]  # 5(다섯)개수 값으로 이루어진 리스트
# for 순서있는값 in 리스트변수:
#     pass
for number in numerics:
    pass
    print(number)

 # for 기본 문형
for x in []:
    pass

# 문자 4개 값들로 이루어진 리스트
for x in ["apple", "melon", "banana", "cherry"]: # 반복 대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(x))

list_fruits = ["apple", "melon", "banana", "cherry"]
for str_fruit in list_fruits: # 반복 대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(str_fruit))

numerics = [0, 1, 2, 3, 4]  # 5(다섯)개수 값으로 이루어진 리스트
for number in numerics:
    pass
    # print("Number : {}".format(number))
    print("Number : {}".format(number+2))


## 답변 설문 받기
# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?          index 0
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타    index 1
# 당신의답변 : A
# 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?          index 2
# A. Python B. Java C. JavaScript D. C++ E. 기타       index 3
# 당신의답변 : D
# 3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?    index 4
# A. Python B. Java C. JavaScript D. C++ E. 기타       index 5 
# 당신의답변 : E


list_polls = ["1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
            ,"A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
            ,"2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
            ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
            ,"3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?"
            ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
            ]

list_statistics = [0, 0, 0, 0, 0]   # 답항만큼 0을 넣어줌
for num_count in [0,2,4]:
    # str_content = list_polls[num_count]
    # print("{}".format(str_content))
    str_question = list_polls[num_count] #0,2,4문항
    print("{}".format(str_question))
    str_answer = list_polls[num_count+1] #변수의값+1, 1,3,5답항
    print("{}".format(str_answer))

    str_question_result = input("당신의답변(A~E를 순서에 맞게 번호로 입력) : ")
    num_question_result = int(str_question_result)  # 문자를 숫자로 변환
    index = num_question_result - 1 # index 위치값 적용
    list_statistics[index] = list_statistics[index] + 1


    print("----------------------------")
    pass

print("선호 답항 : {}".format(list_statistics))
print("End Program!")