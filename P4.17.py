number = int(input("정수를 입력하세요: "))

#카운트를 0으로 초기화한다.
count = 0

# i는 2부터 시작해 number까지 간다
for i in range(2, number+1):
    #  프로그램은 1부터 i까지의 수로 i를 나눠본다. 카운트가 둘 뿐이면 i를 출력한다
    for j in range(1, i+1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(i)
        allCount += 1
    
    # 카운트를 0으로 초기화한다.
    count = 0

## 소수는 1과 자기 자신으로만 나누어지는 수    