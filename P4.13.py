## 정수를 하나 읽어서 이 정수의 이진수 표현을 역순으로 출력하는 프로그램을 작성하라.
# 먼저 number % 2를 출력한다. 다음 number을 number // 2로 바꾼다. 
# 이 과정을 number가 0이 될 때 까지 반복한다.

number = int(input("정수를 입력하세요: "))

if number == 0:
    print(0)

while number != 0:
    print(number % 2)
    number = number // 2
    
