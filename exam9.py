# input() 함수 명령 프롬프트에서 사용자로부터 데이터 입력받을때 사용
# 입력되는 데이터는 문자로 처리된다
'''
string = input("인사말을 입력하세요:")
print(string)

number = input("숫자를 입력하세요 : ")
print(number)
print(type(number)) # 입력되는 타입 : str 
print(number+100) # TypeError
print(int(number)+100)
print(float(number)+100)
'''
# int()함수   : 문자열을 int자료형으로 변환
# float()함수 : 문자열을 float자료형으로 변환
'''
string_a = input("입력 A > ")
int_a = int(string_a)

string_b = input("입력 B > ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("문자열 자료:", int_a + int_b)
'''

#int("안녕하세요") # ValueError
#float("안녕하세요") # ValueError


number = int(12345)
number += 10
print(number)

number = int(52.123)
print(number)

# 정수형 문자열 또는 실수형 문자열을 타입에 맞게 변환할수 있지만
# 타입이 맞지 않은 경우 오류가 발생
#number = int("52.123") # ValueError
#print(number) 

number = int("52") 
print(number) 

number = float("52.123") 
print(number) 

# 하지만 정수 또는 실수를 문자열로 바꾸는 것은 허용한다.
output_a = str(52)
output_b = str(52.273)
print(type(output_a))
print(type(output_b))


raw_input = input("inch단위의 숫자를 입력해 주세요 :")
inch = int(raw_input)
cm = inch * 2.54

print(inch, "inch는 cm단위로", cm , "cm 입니다.")


