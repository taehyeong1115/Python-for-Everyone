RATE_SINGLE_OVER_0 = 0.10
RATE_SINGLE_OVER_8000 = 0.15
ADDTAX_SINGLE_OVER_8000 = 800
RATE_SINGLE_OVER_32000 = 0.25
ADDTAX_SINGLE_OVER_32000 = 4400

RATE_MARRIED_OVER_0 = 0.10
RATE_MARRIED_OVER_16000 = 0.15
ADDTAX_MARRIED_OVER_16000 = 1600
RATE_MARRIED_OVER_64000 = 0.25
ADDTAX_MARRIED_OVER_64000 = 8800

income = float(input("당신의 소득을 입력해주세요: "))
maritalStatus = input("미혼이면 s, 기혼이면 m을 입력해주세요: ")

tax = 0.0

if maritalStatus == "s" :
    if income > 32000 :
        tax = ADDTAX_SINGLE_OVER_32000 + income * RATE_SINGLE_OVER_32000
    elif income > 8000 :
        tax = ADDTAX_SINGLE_OVER_8000 + income * RATE_SINGLE_OVER_8000
    else :
        tax = income * RATE_SINGLE_OVER_0

else :
    if income > 64000 :
        tax = ADDTAX_MARRIED_OVER_64000 + income * RATE_MARRIED_OVER_64000
    elif income > 16000 :
        tax = ADDTAX_MARRIED_OVER_16000 + income * RATE_MARRIED_OVER_16000
    else :
        tax = income * RATE_MARRIED_OVER_0

print(tax)