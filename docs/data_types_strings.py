# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타

# 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?
# A. Python B. Java C. JavaScript D. C++ E. 기타

# 3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?
# A. Python B. Java C. JavaScript D. C++ E. 기타

# 단순 출력 with 변수
# str_first = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
# print(str_first)
# str_second="A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
# print(str_second) 
# print()
# str_third = "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
# print(str_third)
# str_fourth = "A. Python B. Java C. JavaScript D. C++ E. 기타"
# print(str_fourth)
# print("---------------------------------------------------------------------------------------")
# print ("{} -> {}".format(str_third, str_fourth))
# print("---------------------------------------------------------------------------------------")
# # 하나의 변수 사용 출력 with 변수
# str_anyone = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
# print(str_anyone)
# str_anyone = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
# print(str_anyone)
# print() # 한 줄 띌 떄 사용
# str_anyone = "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
# print(str_anyone)
# str_anyone = "A. Python B. Java C. JavaScript D. C++ E. 기타"
# print(str_anyone)
# print("---------------------------------------------------------------------------------------")
# # 두 개 이상 변수 사용 출력 with 변수
# str_question = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
# print(str_question)
# answer = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
# print(answer)
# str_question = "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
# print(str_question)
# answer = "A. Python B. Java C. JavaScript D. C++ E. 기타"
# print(answer)
# str_question = "3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?"
# print(str_question)
# #  = "A. Python B. Java C. JavaScript D. C++ E. 기타"
# print(answer)

# print("---------------------------------------------------------------------------------------")
# # 단순 출력 with 변수
# str_first = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
# print(str_first)
# str_second="A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
# print(str_second) 
# print()
# str_third = "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
# print(str_third)
# str_fourth = "A. Python B. Java C. JavaScript D. C++ E. 기타"
# print(str_fourth)
# print("---------------------------------------------------------------------------------------")
# print ("{} -> {}".format(str_third, str_fourth))


# 다중 변수 정의와 값 넣기
multi_val = 3,5
# multi_val
# (3, 5)

num_first, num_second = 3,5
num_first
# 3
num_second
# 5

# string split()
first, second = "6 8".split()
num_first, num_second = int(first), int(second)
pass