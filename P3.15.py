numberA = float(input("첫번째 수를 입력하세요: ")) 
numberB = float(input("두번째 수를 입력하세요: ")) 
numberC = float(input("세번째 수를 입력하세요: "))

if numberA > numberB :
    if numberA > numberC :
        print("가장 큰 숫자는 " + str(numberA) + "입니다")
    else :
        print("가장 큰 숫자는 " + str(numberC) + "입니다")
        
elif numberB > numberC :
    print("가장 큰 숫자는 " + str(numberB) + "입니다")

else :
    print("가장 큰 숫자는 " + str(numberC) + "입니다")