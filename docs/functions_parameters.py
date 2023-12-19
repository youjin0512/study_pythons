# function에 들어가는 값들
def add(first, second) :  # 호출 시 변수에 값이 할당됨. 여기에서의 first, second는 변수 & 호출할때만 값이 할당됨/입력값에 따라 return되는 값이 달라짐
  sum = first + second
  # return 0
  return sum # 상수(예.0) 대신 변수 사용

# first = 5
# second = 4

if __name__ == "__main__" : 
  # num_sum = 0
  num_sum = add(5, 4) # 5,4는 상수 parameters 사용/ 상수는 왠만하면 사용하지 말고 변수를 사용하자. (변수는 2열의 first, second)
  print("add return 결과 : {}".format(num_sum))
  third = 6   # 변수
  fourth = 10 # 변수
  num_sum = add(third, fourth) # function 부르(call)면 (변수가 아닌) 값들만 전달됨
  print("add return 결과 : {}".format(num_sum))



# 내 점수 넣으면 학점이 나오는 function
def return_grade(my_score) :   # 자신을 불렀을 때 값들 들어감(순서대로 매칭)
  my_grade = ''
  if my_score >= 90 : # 90점 이상 : A,
    my_grade = 'A'
  elif my_score > 80 : # 80점 초과 : B
    my_grade = 'B'
  else :               # 나머지 : F
    my_grade = 'F'
  # return_listbyindex() # function 내에서도 fuction 작성 가능
  return my_grade

if __name__ == "__main__" :    # "__main__" : 초기화로 세팅되어있는 함수(아무도 선언하지 않아도 실행되는 파일이 중심이 되어 main function으로 여겨짐)
  # str_grade = return_grade(99)  # 호출 시 값들이 넘어감(순서 매칭)
  # print("당신의 학점 : {}.".format(str_grade))
  my_score = 88
  str_grade = return_grade(my_score)
  print("당신의 학점 : {}.".format(str_grade))