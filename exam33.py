numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,7,2,3]

# Dictionary만들기
count = {}

for number in numbers:
    #if number in count:
    if count.get(number) != None:
       count[number] = count[number] + 1
    else:
       count[number] = 1

print(count)    


