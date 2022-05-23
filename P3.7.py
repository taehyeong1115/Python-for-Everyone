number1 = float(input("첫번째 수를 입력하세요: "))
number2 = float(input("두번째 수를 입력하세요: "))
number3 = float(input("세번째 수를 입력하세요: "))

if number1 <= number2 and number2 <= number3 :
    print("in order")
    
elif number1 >= number2 and number2 >= number3 :
    print("in order")
    
else :
    print("not in order")