# condition이 True 동안 동작
# while True :
#     pass


# while 정지 1st case with break문 사용
num_virtual = 0
bool_flag = True
while True :
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    if num_virtual >= 5:
        pass
        break 
    pass

# while 정지 2nd case without break문 사용
num_virtual = 0
while num_virtual < 5 :
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    pass

print("End Program!")