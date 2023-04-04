a = "Hello Python Programming...!"
a.upper() #대문자
a.lower() #소문자


# """ 는 입력한 그대로 출력
input_a = """
          안녕하세요
          문자열의 함수를 알아봅니다.   
"""
print(input_a)
print(input_a.strip()) # 양옆의 공백 제거

# lstrip, rstrip
print(input_a.lstrip())  # 왼쪽 공백제거
print(input_a.rstrip())  # 오른쪽 공백제거

print("TrainA".isalpha()) # 영어, 한글이면 true
print("TrainA11".isalpha()) 
print("TrainA10".isalnum()) #영어, 한글, 숫자이면 true
print("Tr!!!!".isalnum()) 
print("10".isdigit()) # 숫자이면 true
print("aaa".isdigit()) 


output_a = "안녕하세요".find("안") # 해당하는 문자의 위치 찾기
print(output_a)
output_b = "안녕안녕하세요".rfind("안") # 해당하는 문자의 위치 찾기
print(output_b)









