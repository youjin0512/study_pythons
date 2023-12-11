# 기본 if 구문
if True : 
    pass

# 기본 if - else 구문
if True : 
    pass
else :
    pass

# 기본 if - elif - else 구문
if True : 
    pass
elif True : 
    pass
else :
    pass

# 질문 형식(conditon,상태) = 변수 + 부등호 + 기준값
# 문자에 대한 긍정으로 질문
str_name = "youjin kim"
if str_name == "youjin kim" : 
    pass
    print("name is {}.".format(str_name))

# 문자에 대한 부정으로 질문
if str_name != "youjin kim" : 
    pass
    print("name is not {}.".format(str_name))

# if - else
# num_first >= 4  -> True : 큼, Flase : 작음
num_first = 5
# if num_first >= 4 :  # 무조건 둘 중 하나 표현
if num_first >= 6 :  # 무조건 둘 중 하나 표현
    pass     # condition이 True이면 실행
    print("{}는 4보다 크다.".format(num_first))
else :
    pass     # condition이 False이면 실행
    print("{}는 4보다 작다.".format(num_first))

# if - elif - else
# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B, 나머지 : F
# my_score = 90
my_score = 79

if my_score >= 90 : # 90점 이상 : A,
    pass
    print("{}은 90점 이상으로 A학점.".format(my_score))
elif my_score > 80 : # 80점 초과 : B
    pass
    print("{}은 80점 초과로 B학점.".format(my_score))
else :               # 나머지 : F
    pass
    print("{}은 80점 이하이므로 F학점.".format(my_score))


# 부등호 사용 시 결과는 True or False(boolean)
# 논리 연산자(True or False에 대한 결과값)
first = 200
second = 33
third = 500
# condition(조건문) 사용 이전에 각각 결과 확인(DEBUG CONSOLE 통해서)
first > second
# True
third > first
# True
(first > second) and (third > first)
# True

if (first > second) and (third > first) :
    print("Both conditions are True")

if not (first < second) :
    print("not (first < second)")
# False

# (first > second) or (third > first) and (first > second) and (third > first)
# 조합해서 쓰는것보다는 하나의 연산자만 사용하는 것이 좋음

pass
print("End Program!")