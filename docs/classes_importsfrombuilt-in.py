import os      # class를 instance화 시킨 상태

# 현재 폴더 위치 CLI : pwd
current_folder = os.getcwd()       # getcwd에 마우스 커서 올려놓고 설명 떴을때 Alt키 누르면 설명 나옴 --> API의 모음 = library boot를 모아놓음
print('현재 실행되는 python 위치 : {}'.format(current_folder))

# 현재 폴더 있는 파일과 폴더 리스트 출력
file_folder_list = os.listdir(current_folder)  # listdir = 어느 폴더인지 지정
print('파일과 폴더 리스트 : {}'.format(file_folder_list))
pass