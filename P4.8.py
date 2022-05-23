## 단어를 하나 읽어서 단어의 각 문자를 다른 줄에 출력하는 프로그램을 작성하라.

# 문자열 입력받기
string = input("단어를 입력하세요: ")

# 반복한다. 문자열의 길이만큼. 
for i in range(len(string)):
    # 무엇을? string의 인덱스 i에 있는 문자를 출력하는 것을.
    print(string[i])