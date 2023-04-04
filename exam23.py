list_a=[1,2,3]

print("리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)

print(list_a)

print("#리스트 중간에 요소 추가하기")
list_a.insert(0, 99)
print(list_a) # [99,1,2,3,4,5]

list_a.extend([6,7,8])
print(list_a) # [99, 1, 2, 3, 4, 5, 6, 7, 8]

del list_a[0]
print(list_a) # [1, 2, 3, 4, 5, 6, 7, 8]

list_a.pop(2)
print("pop(2):", list_a) # [1, 2, 4, 5, 6, 7, 8]

del list_a[3:7]
print(list_a) # [1, 2, 4]

del list_a[:3]
print(list_a) # []

list_a.append(1)
list_a.append(2)
list_a.append(2)
print(list_a) # [1, 2, 2]

list_a.remove(2)
list_a.remove(1)
print(list_a) # [2]

list_a.clear()
print(list_a) # []

'''
list_a.reverse()
print(list_a) # [2, 1]
'''

