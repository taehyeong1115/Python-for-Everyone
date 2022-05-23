line = str(input("문자열을 입력하세요: "))

if line.isalpha() :
    print("알파벳 문자만 포함합니다")
if line.isupper() :
    print("대문자만 포함합니다")
if line.islower() :
    print("소문자만 포함합니다")
if line.isdigit() :
    print("숫자만 포함합니다")
if line.isalnum() :
    print("문자와 숫자만 포함합니다")
if line.startswith("A") or line.startswith("B") or line.startswith("C") or line.startswith("D") or line.startswith("E") or line.startswith("F") or line.startswith("G") or line.startswith("H") or line.startswith("I") or line.startswith("J") or line.startswith("K") or line.startswith("L") or line.startswith("M") or line.startswith("N") or line.startswith("O") or line.startswith("P") or line.startswith("Q") or line.startswith("R") or line.startswith("S") or line.startswith("T") or line.startswith("U") or line.startswith("V") or line.startswith("W") or line.startswith("X") or line.startswith("Y") or line.startswith("Z"):
    print("대문자로 시작합니다")
if line.endswith(".") :
    print("마침표로 끝납니다")