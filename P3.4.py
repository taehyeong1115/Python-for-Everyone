# 수 세 개 입력받기
number1 = float(input("첫번째 수를 입력하세요: "))
number2 = float(input("두번째 수를 입력하세요: "))
number3 = float(input("세번째 수를 입력하세요: "))

# 모두 같으면 모두 동일을 출력
if number1 == number2 and number2 == number3 :
    print("모두 동일")
# 그게 아니라면 모두 다른지 확인하고 다르면 모두 다름 출력    
elif number1 != number2 and number2 != number3 and number3 != number1 :
    print("모두 다름")
# 그것도 아니라면 그냥 아무것도 아님을 출력
else :
    print("아무것도 아님")