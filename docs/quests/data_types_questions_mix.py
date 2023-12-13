# * quests
# docs/quests/data_types_questions_mix.py
# - 문제 작성 : 직접 입력
# - 출력 : print(mixed_questions)
# 최소 1개 function 사용

def get_question():
    question_info = {"question": "", "answers": ["", "", "", ""], "correct_answer": "", "score": ""}
    question_info["question"] = input("문제를 입력하세요: ")
    for i in range(4):
        question_info["answers"][i] = input(str(i+1) + "번 보기를 입력하세요: ")
    question_info["correct_answer"] = int(input("정답 번호를 입력하세요: "))
    question_info["score"] = int(input("배점을 입력하세요: "))
    return question_info
mixed_questions = []
for i in range(3):
    print(str(i+1) + "번 문제")
    question = get_question()
    mixed_questions.append(question)
print(mixed_questions)