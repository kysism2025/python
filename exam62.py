def power(item):
    return item*item

def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

# map()함수 : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성
output_a = map(power, list_input_a)
print("#map()함수 실행 결과")
#print(output_a)
#print(list(output_a)) # [1, 4, 9, 16, 25]

output_b = map(under_3, list_input_a)
#print(output_b)
#print(list(output_b)) # [True, True, False, False, False]

'''
for i in output_a:
    print(i)

for i in output_b:
    print(i)    
'''    

# filter()함수 : 리스트의 요소를 함수에 넣고 리턴된 값이 true인 것으로, 새로운 리스트를 구성
output_c = filter(under_3, list_input_a)
print("#filter()함수 실행 결과")
# print(output_c)
# print(list(output_c))    # [1,2]


