## 단어를 하나 읽어서 그 단어의 모든 부분 문자열을 길이 순서대로 출력하는 프로그램을 작성하라.

# 문자열을 입력받는다

# 문자열의 길이만큼 반복 / i
    # 문자열의 길이 - i 만큼 반복 / j
        # i + 1 만큼 반복 / k
            #string[k + j]를 옆으로 출력
        # 줄바꿈
    
string = input("문자열을 입력하세요: ")

for i in range(len(string)):
    for j in range(len(string) - i):
        for k in range(i + 1):
            print(string[k + j], end = '')
        
        print("")

