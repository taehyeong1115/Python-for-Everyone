RATE1 = 0.01
RATE2 = 0.02
RATE3 = 0.03
RATE4 = 0.04
RATE5 = 0.05
RATE6 = 0.06

RATE2_OVER_THAN = 50000
RATE3_OVER_THAN = 75000
RATE4_OVER_THAN = 100000
RATE5_OVER_THAN = 250000
RATE6_OVER_THAN = 500000

income = float(input("소득을 입력해주십시오: "))

tax = 0.0

if income >= RATE6_OVER_THAN :
    tax = RATE6 * income
elif income >= RATE5_OVER_THAN :
    tax = RATE5 * income
elif income >= RATE4_OVER_THAN :
    tax = RATE4 * income
elif income >= RATE3_OVER_THAN :
    tax = RATE3 * income
elif income >= RATE2_OVER_THAN :
    tax = RATE2 * income
else :
    tax = RATE1 * income
    
print(tax)