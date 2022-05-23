stringA = str(input("첫번째 문자열을 입력해주세요: "))
stringB = str(input("두번째 문자열을 입력해주세요: "))
stringC = str(input("세번째 문자열을 입력해주세요: "))

if stringA < stringB :
    if stringA < stringC :
        if stringB < stringC :
            print(stringA)
            print(stringB)
            print(stringC)
        else :
            print(stringA)
            print(stringC)
            print(stringB)
            
    else :
        print(stringC)
        print(stringA)
        print(stringB)
        
elif stringB < stringC :
    if stringA < stringC :
        print(stringB)
        print(stringA)
        print(stringC)
    else :
        print(stringB)
        print(stringC)
        print(stringA)

else :
    print(stringC)
    print(stringB)
    print(stringA)