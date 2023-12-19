import functions_parameters   # functions_parameters.py에 있는 걸 호출(import)

if __name__ == "__main__" :   # "__main__" : 모든 프로그램의 중심(무조건 하나 존재)
    # import functions in another file
    num_result = functions_parameters.add(4, 5)
    print("result : {0}".format(num_result))
    pass

# function중의 function(최고참) - 안써도 있는 존재