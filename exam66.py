
with open("info.txt", "r") as file:
    for line in file:
        
        # strip() : 문자열 앞뒤에 있는 공백 제거
        # split() : 문자를 구분
        (name, weight, height) = line.strip().split(",")
        
        if(not name) or (not weight) or (not height):
            continue
        
        bmi = int(weight) / (int(height)*int(height))

        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print("\n".join([
            "이름:{}",
            "몸무게:{}",
            "키:{}",
            "BMI:{}",
            "결과:{}"
        ]).format(name, weight, height, bmi, result))
        print()

