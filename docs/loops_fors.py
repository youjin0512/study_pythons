# 얼마만큼 반복할지에 대한 '값들'을 알려줌
numeric = 0
numerics = [0, 1, 2, 3, 4]  # 5(다섯)개수 값으로 이루어진 리스트
# for 순서있는값 in 리스트변수:
#     pass
for number in numerics:
    pass
    print(number)

 # for 기본 문형
for x in []:
    pass

# 문자 4개 값들로 이루어진 리스트
for x in ["apple", "melon", "banana", "cherry"]: # 반복 대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(x))

list_fruits = ["apple", "melon", "banana", "cherry"]
for str_fruit in list_fruits: # 반복 대상 리스트 직접 넣기
    pass
    print("fruit name : {}!".format(str_fruit))

numerics = [0, 1, 2, 3, 4]  # 5(다섯)개수 값으로 이루어진 리스트
for number in numerics:
    pass
    # print("Number : {}".format(number))
    print("Number : {}".format(number+2))

print("End Program!")