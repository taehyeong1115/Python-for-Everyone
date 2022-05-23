## 단어를 하나 읽어서 그 단어에 나오는 모음의 수를 출력하는 프로그램을 작성하라.

# 문자열을 입력받는다 
string = input("단어를 입력하세요: ")

# 모음을 카운트할 정수 변수를 0으로 초기화한다
vowelsCount = 0

# 반복한다 문자열의 길이만큼 
for i in range(len(string)):
#   인덱스 i의 문자가 a e i o u y A E I O U 와 같으면 카운트를 추가
    if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" or string[i] == "y" or string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U" or string[i] == "Y":
        vowelsCount += 1

# vowelsCount를 출력
print(str(vowelsCount) + " vowels")