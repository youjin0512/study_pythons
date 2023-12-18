# 기본 구문
try:
    pass    # 업무 코드 입력 부분                                
except:
    pass    # 업무 코드 문제 발생 시 대처 코드
finally :
    pass    # try나 except이 끝난 후 무조건 실행 코드

# 콜론(:)이 있으면 값을 여러 개 넣을 수 있음.
# e.g. 분모를 0으로 나눌 때 오류 -> 방어코드를 입력해야 오류나지 않음


# pure python with 계산기
# 숫자를 무한대로 받아서 두 개를 덧셈으로 만드는 프로그램 만들기(계산기만들기)

# num_first = '4'
num_first = 4
num_second = 5

# 곱셈 연산
try:
    result = num_first / num_sec ond    # 정상일 때 뱉어내는 부분 -> 해당 부분 정상이면바로 아랫줄 pass로 넘어감, but num_first가 문자이므로 except의 result로 넘어감(breakpoint 후 F5시)
    pass    # 업무 코드 입력 부분                                
except:
    result = int(num_first) / int(num_second)    # 에러날 때 캐스트로 해서 뱉어내는 부분 / num_first, num_second를 int로 감싸기
    pass    # 업무 코드 문제 발생 시 대처 코드
finally :
    pass    # try나 except이 끝난 후 무조건 실행 코드


print("{} = {} * {}".format(result, num_first, num_second ))
# num_first = '4'
# num_second = 5
# print("{} = {} * {}".format(result, num_first, num_second ))
# 터미널 출력값 : 0.8 = 4 * 5
pass