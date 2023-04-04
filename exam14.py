# in 연산자 : 문자열 내부에 어떤 문자열이 있는지 확인할 때 사용
print("안녕" in "안녕하세요") # 찾고자 하는 문자열이 존재하기에 true
print("잘자" in "안녕하세요") # 찾고자 하는 문자열이 존재하지 않기에 false

# split()함수 : 문자열을 특정한 문자로 자름
a="10,20,30,40,50".split(",") # 공백을 이용한 분리
print(a)
a="10 20 30 40 50".split(" ")
print(a)

# Python 3.6.부터 사용
print("{}".format(10))
print(f'{10}')

print(f"3+4={3+4}")

data=['별',2,'M','경기도 안산시 중앙동','Y']
"""
이름 : {}
나이 : {}
성별 : {}
지역 : {}
중성화 여부 : {}
""".format(*data)
print(*data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
