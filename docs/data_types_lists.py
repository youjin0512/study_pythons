numeric_first = 0
numeric_second = 1
numeric_third = 2
numeric_fourth = 3
numeric_fifth = 4

# 사용 이유 : 값들의 모임을 쉽게 전달
# 숫자 5개 값들로 이루어진 리스트
list_numerics = [0, 1, 2, 3, 4]
# 문자 3개 값들로 이루어진 리스트
list_fruits = ["apple", "banana", "cherry"]
# 숫자와 문자 섞은 리스트 -> 가능은 하나, **우린 쓰지 않는다.**
list_mixs = [0, 1, 2, 3, "apple", "banana"]

# DEBUG COLSOLE
len(list_numerics)
# 5
len(list_mixs)
# 6

## for문 활용 후 다시 오기

# index(색인, 위치값)
list_fruits = ["melon", "apple", "banana", "cherry"]
## index로 값 가져오기
list_fruits[0] # 단일 변수로 여김 ; 1차원(행) 단일 변수
# 'melon'
list_fruits[3]
# 'cherry'

## error 발생
# list_fruits[4]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range

# list 초기화 방식
list_fruits_primitive = ["melon", "apple", "banana", "cherry"]   # primitive : 약속어
tuple_fruits = ("melon", "apple", "banana", "cherry")
list_fruits_constructor = list(("melon", "apple", "banana", "cherry"))   # constructor : 생성자 / list는 import 필요없음. 외부에서 class를 끌어안고 들어옴   *list() : class
# list_fruits_primitive.append('strawberry')            # append : 맨 뒤에 붙는다(넣는다)

type(list_fruits_primitive)
# <class 'list'>
type(list_fruits_constructor)
# <class 'list'>

# 삭제 대상이 해당 값이 있는 item
## append 뒤에 문자열 추가
list_fruits_primitive.append('strawberry')
list_fruits_constructor.append('watermelon')
## remove 해당 문자열 삭제
list_fruits_primitive.remove('apple')
list_fruits_constructor.remove('melon')
# 삭제 대상이 전체 item
list_fruits_primitive.clear()

pass