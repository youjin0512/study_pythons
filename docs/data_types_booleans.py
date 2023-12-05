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
##같이 않음 기호 '!=' (띄어쓰기 유무로 true/false 판단)
str_name != "youjinkim"
# True
str_name != "youjin kim"
# False