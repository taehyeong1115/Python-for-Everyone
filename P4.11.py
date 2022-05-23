## 단어를 하나 읽어서 그 단어의 음절 수를 출력하는 프로그램을 작성하라. 
# a e i o u y 모음들이 연속해 나오면 마지막 e를 제외하고 전체를 하나의 음절로 본다. 
# 만약 결과가 0이 나오면 1로 바꾼다.

# 문자열을 입력받는다
string = input("문자열을 입력하세요: ")

# 카운트를 0으로 초기화
count = 0

# 끝에서 두번째 문자열까지 반복한다
for i in range(len(string) - 1):
    #aeiouy와 같은지 검사한다
    if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" or string[i] == "y" or string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U" or string[i] == "Y":
        # 만약 i가 끝에서 두번째의 인덱스이고
        if i == len(string) - 2:
            # 맨 끝 문자가 e라면
            if string[len(string) - 1] == "e":
                #카운트에 1을 추가한다
                count += 1
        # 맞으면 뒤 문자열에 모음이 있는지 검사한다. 없으면 카운트 있으면 넘긴다
        if string[i + 1] == "a" or string[i + 1] == "e" or string[i + 1] == "i" or string[i + 1] == "o" or string[i + 1] == "u" or string[i + 1] == "y" or string[i + 1] == "A" or string[i + 1] == "E" or string[i + 1] == "I" or string[i + 1] == "O" or string[i + 1] == "U" or string[i + 1] == "Y":
            continue
        else:
            count += 1
        
# 만약 마지막 문자가 aiouy와 같다면 카운트에 1을 추가
if string[len(string) - 1] == "a" or string[len(string) - 1] == "i" or string[len(string) - 1] == "o" or string[len(string) - 1] == "u" or string[len(string) - 1] == "y" or string[len(string) - 1] == "A" or string[len(string) - 1] == "I" or string[len(string) - 1] == "O" or string[len(string) - 1] == "U" or string[len(string) - 1] == "Y":
    count += 1
# 카운트가 0이라면 1로 바꾼다
if count == 0:
    count = 1

print(count)

