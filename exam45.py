list_a = [1,2,3]
print(list_a)
list_a.reverse()
print(list_a)

list_reversed = reversed(list_a)
print(list_reversed)
print(list(list_reversed))

print("# reversed() 함수 반복문")
print("for in reversed([1,2,3,4,5])")

list_a = [1,2,3]
for i in reversed(list_a):
  print("-",i)