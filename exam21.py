'''
number = input("정수 입력")
number = int(number)


# 실행을 할 것이 없다고 할때 pass라는 키워드를 사용한다.
if number > 0:
   pass # 임시적으로 비워둘때
else :
   pass
'''

# 리스트 : 여러가지 자료를 저장할 수 있는 자료
array=[273, 32, 103, "문자열", True, False]
print(array)
print(array[0])
print(array[:5])

array[0] = "change"
print(array[0])
print(array[3][0:3])
print(array[3][0])

list_a = [[1,2,3],[4,5,6],[7,8,9]]
print(list_a[0])
print(list_a[1][0])
# print(list_a[4]) # indexError


