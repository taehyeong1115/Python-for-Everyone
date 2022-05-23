number1 = float(input("첫번째 수를 입력하세요: "))
number2 = float(input("두번째 수를 입력하세요: "))
number3 = float(input("세번째 수를 입력하세요: "))
number4 = float(input("네번째 수를 입력하세요: "))

# AABB ABAB ABBA

if (number1 == number2 and number3 == number4) :
    print("two pairs")
    
elif number1 == number3 and number2 == number4 :
    print("two pairs")
    
elif number1 == number4 and number2 == number3 :
    print("two pairs")
    
else :
    print("not two pairs")