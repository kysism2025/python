array = []
count = 0

for i in range(0, 20, 2):
    array.append(i**2)
    print("i = ", array[count])
    count += 1
print(array)  

array = [i for i in range(0,20)]
print(array)  
    
array = [i*i for i in range(0,20, 2)]
print(array)  


array=["사과","자두","초콜릿","바나나","체리"]
output1=[fruit for fruit in array if len(fruit) is 2]
output2=[fruit for fruit in array if fruit != "초콜릿"]
print(output1)
print(output2)



    