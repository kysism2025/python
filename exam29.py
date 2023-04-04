numbers = [1,2,3,4,5,6,7,8,9]

'''
# 짝수 번째 요소의 값을 제곱한다.
for i in range(0, len(numbers)): # 0 ~ 8
    if(i % 2 == 1):
        numbers[i] = numbers[i]**2   
    
print(numbers)
'''
'''
cnt = 0
for i in range(0, len(numbers)): # 0 ~ 8
    if i % 2 == 1:
     numbers[i] = numbers[i]**2   
    else:
     # j=cnt*2+1
     print("i={}, j={}".format(cnt, numbers[i]))
     cnt = cnt + 1
    
print(numbers)
'''

for i in range(0, len(numbers)//2): 
    j=i*2+1
    #print("i={}, j={}".format(i, j))
    print(f"i={i}, j={j}") # f-string ver3.6
    numbers[j] = numbers[j]**2

print(numbers)
