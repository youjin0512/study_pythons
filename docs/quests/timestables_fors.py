# - 구구단 5단 단계별 표시(for 문 사용)
# 예. 5 * 1= 5  5 * 2 = 10 ... 5 * 9 = 45

num_put = int(input())
num_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num_put in num_lists:
    print("5*{}={}".format(num_put, 5*num_put))