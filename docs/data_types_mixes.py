# list 안에 dict

# key(str) : value(여러 변수 종류 가능)              # key : 주로 문자(str)->'' 또는 " "
dict_carinfor_mustang = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price": 30000
}

dict_carinfor_sonata = {
        "brand": "Hyundai",
        "model": "Sonata",
        "year": 2020,
        "color": "Black",
        "price": 30000
}

list_carinfor = [dict_carinfor_mustang, dict_carinfor_sonata]

list_carinfor = [         # 맨 처음 : list가 싸고 있음, 두 번째 : dictionary, 세 번째 : key와 value로 싸고 있음
    {
    "brand": "Ford",     
    "model": "Mustang",
    "year": 1964,
    "color": "Red",
    "price": 30000
    },
    {
    "brand": "Hyundai",
    "model": "Sonata",
    "year": 2020,
    "color": "Black",
    "price": 30000
    }
]

pass
dict_carinfo_k5 = {
        "brand": "Kia",
        "model": "K5",
        "year": 2021,
        "color": "White",
        "price": 28000
    }

list_carinfor.append(dict_carinfo_k5)
pass


# list_carinfor안에 있는 index 0번에 있는 "model" : "Mustang" 접근 방법
dict_carinfor_index_first = list_carinfor[0]    # 출력시 data type은 dictionary  # [0]은 인덱스로 첫 번째라는 뜻.
dict_carinfor_index_first['model']
pass
list_carinfor[0]['model']   # 대괄호를 연속으로 사용한다는 것은 한 번 접근하고, 두 번 접근한다는것.
pass

# for로 각 dict 정보 출력
for dict_carinfor in list_carinfor:
    brand = dict_carinfor['brand']
    model = dict_carinfor['model']
    print('브랜드 : {}, 모델 : {}'.format(brand, model))
    # print(dict_carinfor)
    pass