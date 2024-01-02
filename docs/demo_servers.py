def home(value) :
    html = "<body> It's Home, Value {} </body>".format(value)
    return html

def error(value) :
    html = "<body> It's Error, value {} </body>".format(value)
    return html
# 항시 응답하는 프로그램
while True : 
    work, value = input('업무 / 해당값 : ').split()
    print("work : {}, value : {}".format(work, value))
    if work == 'home' :
        result = home(value)          # 업무를 home을 넣으면 호출
        print(result)
    else :
        result = error(value)         # 업무를 home이 아닌것을 넣으면 에러
        print(result)