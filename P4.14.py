## 평균과 표준편차. 여러 개의 부동 소수점 숫자를 읽는 프로그램을 작성하라.

number = 0.0

sum = 0.0

squaresSum = 0.0

count = 0

while number != "stop":
    number = input("실수를 입력하세요. 멈추려면 stop을 입력하세요: ")
    if number.isdigit():
        number = float(number)
        sum += number
        squaresSum += number ** 2
        count += 1

print("")
print("평균은", sum / count , "입니다")
print("")
print("표준 편차는", ((squaresSum - sum ** 2 / count) / (count - 1)) ** (1/2) ,"입니다.")