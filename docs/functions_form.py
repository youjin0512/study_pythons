# 기본 function 형식 - 기다림. 불리울 때 기능한다.
def function_name() : 
  pass      # 내용 넣기
  return 0

## 그냥 연습
def my_function():
  print("Hello from a function")

## function 부르기
my_function()
pass

# 문항1과 답항을 출력하는 function (기능부여된 상태)
def print_question_and_answer() :  
  str_anyone = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
  print(str_anyone)
  str_anyone = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
  print(str_anyone)
  
  return 0
# print_question_and_answer()  : 콜 하는 방법
# print_question_and_answer()