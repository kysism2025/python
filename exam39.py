'''
i=0
while i < 10:
    print(f"{i}번째 반복입니다.")
    i+=1
'''
list_test = [1,2,1,2]    
value = 2

while value in list_test: #list_test내부에 값이 있으면 true
    list_test.remove(value)

print(list_test)    
    