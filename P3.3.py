# 100억 미만의 정수 입력받기
number = int(input("100억 미만의 정수를 입력하세요: "))

# 입력받은 정수가 음수이면 -1 곱해주기
if number < 0 :
    number *= -1
    
# 입력받은 정수가 10억 이상이면 10자리
if number >= 1000000000 :
    print("이 정수의 자릿수는 10자리입니다") 
    
elif number >= 100000000 :
    print("이 정수의 자릿수는 9자리입니다")
elif number >= 10000000 :
    print("이 정수의 자릿수는 8자리입니다")
elif number >= 1000000 :
    print("이 정수의 자릿수는 7자리입니다")
elif number >= 100000 :
    print("이 정수의 자릿수는 6자리입니다")
elif number >= 10000 :
    print("이 정수의 자릿수는 5자리입니다")
elif number >= 1000 :
    print("이 정수의 자릿수는 4자리입니다")
elif number >= 100 :
    print("이 정수의 자릿수는 3자리입니다")
elif number >= 10 :
    print("이 정수의 자릿수는 2자리입니다")

else :
    print("이 정수의 자릿수는 1자리입니다")