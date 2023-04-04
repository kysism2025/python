numbers=[1,2,3,4,5,6,7,8,9]
output = [[],[],[]] #[1,4,7],[2,5,8],[3,6,9]

'''
for number in numbers:
    if number % 3 == 1:
        output[0].append(number)
    elif number % 3 == 2:
        output[1].append(number)
    elif number % 3 == 0:
        output[2].append(number)

print(output)        
'''

for number in numbers:
    output[(number - 1) % 3].append(number)
print(output)

