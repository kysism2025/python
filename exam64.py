#file = open("basic.txt","w") # write
#file.write("Hello Python Programming...!")
#file.close()

# with open("basic.txt","w") as file:
#     file.write("Test를 합시다")

# file = open("basic.txt","a") # append
# file.write("Hello Hello Hello...!")
# file.close()

# with open("basic.txt","a") as file:
#     file.write("basic basic basic")

# file = open("basic.txt","r")
# s = file.read()
# print(s)
# file.close()

# with open("basic.txt","r") as file:
#     content = file.read()
#     print(content)    

with open("info.txt","r") as file:
     content = file.read()
     print(content)    


'''
try:
    file = open("aaa.txt", "r")
    memo = file.readlines()
    for ln in memo:
        print(ln, end="")
    file.close()
except Exception as e:
    print(e)
else:
    print("오류 없습니다.")
finally:
    print("마지막을 수행하였습니다.")    
'''    




