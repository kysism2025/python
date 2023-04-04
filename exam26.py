a=[1,2,3,4]
b=a
print(type(a), a)
print(type(a[0]), a[0])
print(*a)
print(b)

# 전개 연산자
c=[*a] 
d=[*a, *a]
e=[*a,5,6,7]
print(c)
print(d)
print(e)


'''
리스트(list)  : 여러가지 자료를 저장할 수 있는 자료형  tuple, dict, list
요소(element) : 리스트 내부에 있는 각각의 내용을 의미
인덱스(index) : 리스트 내부에서 값의 위치를 의미
for 반복문    : 특정코드를 반복해서 실행할때 사용하는 기본 구문
'''


