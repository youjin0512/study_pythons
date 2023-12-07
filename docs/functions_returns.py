## call by value
## 나오는 값 처리
# first = 5
# second = 4
# sum = first + second
def add() : 
  first = 5
  second = 4
  sum = first + second
  # return 0
  return sum # 상수(예.0) 대신 변수 사용

# print(add())  #print한다 = add를 통해 return을 호출한다

# num_sum = 0
# print(num_sum)
# 프린트 결과값 0

# num_sum = add()
# print(add())
# 프린트 결과값 0

# return : 값이 나오고 그 값을 활용할 수 있다.
# return 가능한것 : 문자 하나, 숫자 하나, 리스트 묶음

# num_sum = 0
num_sum = add()
print("add return 결과 : {}".format(num_sum))

########################################################################################
# num_first = 4
# num_second = 5
# # 곱셈 연산
# num_first * num_second

# 두 수를 곱해서 결과 return
def multiply() : 
  num_first = 4
  num_second = 5
  # 곱셈 연산
  result = num_first * num_second
  return result

##결과값 20 불러내기
# 방법 1.
# print(multiply())
# 방법 2.
# num_multiply = multiply()
# print(num_multiply)
# 방법 3.
num_multiply = multiply()
print("num_multiply() return value : {}".format(num_multiply))

# list_fruits = ["melon", "apple", "banana", "cherry"]
## index로 값 가져오기
# list_fruits[0] # 단일 변수로 여김 ; 1차원(행) 단일 변수
def return_list() : 
  list_fruits = ["melon", "apple", "banana", "cherry"] # list는 여러개의 값을 갖고 있지만, 묶음 이기 때문에 내용 넣을 수 있음
  return list_fruits
print("return_list() return result : {}".format(return_list())) # return list 옆에 괄호 ()는 함수라는 뜻.

# list 중에 index로 값 return
def return_listbyindex() : 
  list_fruits = ["melon", "apple", "banana", "cherry"]
  return list_fruits[0] # 단일 변수로 여김 ; 1차원(행) 단일 변수
print("return_listbyindex() return result : {}".format(return_listbyindex()))


##if문 바꾸는 방법
# my_score = 79
# if my_score >= 90 : # 90점 이상 : A,
#     print("{}은 90점 이상으로 A학점.".format(my_score))
# elif my_score > 80 : # 80점 초과 : B
#     print("{}은 80점 초과로 B학점.".format(my_score))
# else :               # 나머지 : F
#     print("{}은 80점 이하이므로 F학점.".format(my_score))
# 반복 print 작업을 줄이기 위한 function 만들기
def return_grade() : 
  my_score = 85
  my_grade = ''
  if my_score >= 90 : # 90점 이상 : A,
    my_grade = 'A'
  elif my_score > 80 : # 80점 초과 : B
    my_grade = 'B'
  else :               # 나머지 : F
    my_grade = 'F'
  # return_listbyindex() # function 내에서도 fuction 작성 가능
  return my_grade

str_grade = return_grade()

print("당신의 학점 : {}.".format(str_grade))