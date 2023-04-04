
numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x%2 ==1 , numbers)))


print("# 3이상, 7미만 추출하기")
print(list(filter(lambda x: x >= 3 and x < 7 , numbers)))


print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda x: x**2 < 50 , numbers)))

numbers2 = [1,2,3,4,5,6]
# map(함수, 리스트)
# filter(함수, 리스트)
print("::".join(map(str, numbers2)))


