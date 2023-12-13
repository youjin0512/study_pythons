# Class 초기화 방법
dict_initial = {}    # empty (비어있는 상태)
dict_initial = dict()  # dict() : class name    # empty (비어있는 상태)

list_car_infor = ['Ford', 'Mustang', 1964]    # infor가 붙으면 문자열+숫자 조합으로 사용 가능  # 해당 줄은 index임.



# key(str) : value(여러 변수 종류 가능)              # key : 주로 문자(str)->'' 또는 " "
dict_carinfor = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "items": []
}
model = dict_carinfor["model"]
print('dict_carinfor에 있는 model name : {}'.format(model))



## DEBUG CONSOLE에서 입력한 key(왼쪽)에 대한 value 값(오른쪽)
# key 로 인한 값 변경
dict_carinfor['year'] = 1970
# 새로운 key와 값 정의
dict_carinfor['color'] = "red"
dict_carinfor["color"] = ["red", "yellow", "brown"]


pass