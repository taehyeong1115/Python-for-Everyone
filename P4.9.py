## 단어를 하나 읽어서 그 단어를 거꾸로 출력하는 프로그램을 작성하라.

# 문자열을 입력받고
string = input("단어를 입력하세요: ")

# 역순 문자를 저장할 문자열 선언
reverseString = ""

# 반복한다. 문자열의 길이만큼. 끝 문자 (문자열의 길이 - i) 부터 선언한 문자열에 집어넣는다. 
for i in range(len(string)):
    reverseString += string[len(string) - 1 - i]
    
# 선언한 문자열을 출력한다
print(reverseString)