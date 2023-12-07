# source from ../polls_first/polls_first_youjin.py

# # 완성본
# 1. 상품의 품질에 대해 어떻게 생각하시나요?
# 1. 좋음     2. 중간     3. 좋아지길

# 당신 생각은 몇 번 : 3
# ----------
# 2. 상품의 가격에 대해 어떻게 생각하시나요?    
# 1. 좋음     2. 중간     3. 좋아지길

# 당신 생각은 몇 번 : 2
# ----------
# 3. 상품의 디자인에 대해 어떻게 생각하시나요?    
# 1. 좋음     2. 중간     3. 좋아지길

# 당신 생각은 몇 번 : 3
# ----------
# 4. 상품에 대한 전반적인 만족도는 어떠신가요?    
# 1. 좋음     2. 중간     3. 좋아지길

# 당신 생각은 몇 번 : 1

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer =  ["좋음", "중간", "좋아지길"]
list_statistics = [0, 0, 0]
for num_first in [0,1,2,3]:
    # str_question = list_question[num_first] 
    print("{}. {}".format(num_first+1, list_question[num_first]))

    for num_second in [0,1,2]: 
        # str_answer = list_answer[num_second]
        print(" {}. {}".format(num_second+1, list_answer[num_second]),end="")
    print("")
    print("")

    str_question_result = input("당신 생각은 몇 번 : ")
    num_question_result = int(str_question_result)  # 문자를 숫자로 변환
    index = num_question_result - 1 # index 위치값 적용
    list_statistics[index] = list_statistics[index] + 1

    if num_first < 3 :
        pass 
        print("----------")
    else :
        print("")
    # 설문자 답항별 갯수 표시 : [1, 1, 2]
    print("설문자 답항별 갯수 표시 : {}".format(list_statistics))

# ---- 통 계 ----
# 답변별 가중치 (좋음:3, 중간:2, 좋아지길:1)
# 답항 가중 평균 : 
# (1*3 + 1*2 + 2*1) / (3+2+1) = 0.86

    num_third = 
    str_answer_good = int()