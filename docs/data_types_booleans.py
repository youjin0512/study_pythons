bool_flag = True  # yes 와 동일
pass
# 갈림길에서 '왼쪽으로 갈래?'
# 대답 : 아니!(오른쪽을 의미)
bool_flag = False
type(bool_flag)
# <class 'bool'>

# 문자 판단
# 같음에 대한 기호 '==' (띄어쓰기 유무로 true/false 판단)
str_name = "youjin kim"
str_name == "youjin kim"
# True
str_name == "youjinkim"
# False
##같지 않음 기호 '!=' (띄어쓰기 유무로 true/false 판단)
str_name != "youjinkim"
# True
str_name != "youjin kim"
# False

# 숫자에 대한 판단 (변수 + 부등호 + 기준값)
# 컴퓨터 입장
# True = Yes = 1, False = No = 0

5 == 4
# False
num_first = 5
num_first == 4
# False
num_first != 4
# True
num_first > 4   # 초과
# True
num_first >= 4  # 이상
# True

# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B, 나머지 : F
my_score = 90
my_score >= 90
# True
my_score = 89
my_score >= 90
# False
my_score > 80
# True
my_score = 80
my_score > 80
# False
pass