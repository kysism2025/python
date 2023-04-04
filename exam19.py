# 끝자리로 짝수와 홀수 구분
number = input("<정수 입력>");

last_character = number[-1]
last_number = int(last_character)

print(last_character)

if last_number % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 다음줄에 입력시 '\'을 추가해준다.
if last_number == 0\
   or last_number == 2\
   or last_number == 4\
   or last_number == 6\
   or last_number == 8:
    print("짝수")
else:
    print("홀수")    
