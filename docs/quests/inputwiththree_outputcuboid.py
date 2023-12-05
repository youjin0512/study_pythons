# * quest
# - 가로 * 세로 * 높이 = 직육면체
# - input : 가로 세로 높이  <- 한 줄로 받기
# - output :  가로 * 세로 * 높이 = 직육면체
#           e.g. 가로(4)m * 세로(1)m * 높이(1)m = 직육면체(4)m^3    *m^3 = 문자(세제곱미터)


num_first, num_second, num_third = input().split()
first = int(num_first)
second = int(num_second)
third = int(num_third)
cuboid = first * second * third
print(가로({})m * 세로({})m * 높이({})m = 직육면체({})m^3 .format(first, second, third, cuboid))
pass
# input_width = "가로"
# input_length = "세로"
# input_height = "높이"

# # input
# str_input = input("{} {} {}".format(str_input_width,str_input_length,str_input_height))
# str_input_desc = " = 직육면체"
# print(" = 직육면체".format(str_input = input))

