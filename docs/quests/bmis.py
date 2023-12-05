# - input(두 값은 정수) : 몸무게, 키
# - BMI = 몸무게(kg) / 키(m)^2 
# BMI 분류
#   18 미만 : 저체중
#   18 - 22 : 정상
#   23 - 24 : 과체중
#   25 이상 : 비만

num_first, num_second = input().split()
weight = int(num_first)
height = int(num_second) * 0.01
bmi = weight / (height**2)
print("{}/{}^2={}".format(weight, height, bmi))
if bmi >= 25 :          
    print("{}점은 25점 이상이므로 비만입니다.".format(bmi))
elif bmi >= 23 :       
    print("{}점은 23점 이상이므로 과체중입니다.".format(bmi))
elif bmi >= 18 :       
    print("{}점은 18점 이상이므로 정상입니다.".format(bmi))
else :         
    print("{}점은 18점 미만이므로 저체중입니다.".format(bmi))

print("End Program!")

# print("{}은 80점 초과로 B학점.".format(my_score))