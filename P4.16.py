number = int(input("정수를 입력하세요: "))

# 카운트를 0으로 초기화
count = 0

# i는 2부터 시작해 number까지 반복한다
for i in range(2, number + 1):
    # j는 1부터 i까지 늘어나며
    for j in range(1, i + 1):
        # i를 j로 나눠 소수인지 확인하게 한다
        if i % j == 0:
            count += 1
            
    # i가 만약 소수이면
    if count == 2:
        # number % i == 0 인 동안 
        while number % i == 0:
            # 나눠지면 i를 출력하고 number를 나눈 값으로 저장한다.
            print(i)
            number = number / i
    
    # 남은 숫자가 1이면 루프를 탈출한다.
    if number == 1:
        break
    
    # 카운트를 0으로 초기화
    count = 0