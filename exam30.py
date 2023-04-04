# 딕셔너리(dictionary) : 키를 기반으로 값을 저장하는 것
# 리스트는 index를 기반으로 값을 저장, 표기법 : []을 사용

dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고","설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

dname = dictionary["name"]
dtype = dictionary["type"]
print(f"name:{dname}")
print(f"type:{dtype}")

dictionary["name"] = "8D 건조 망고"
dname = dictionary["name"]
print(f"name:{dname}")

dingredient = dictionary["ingredient"]
print(f"ingredient:{dingredient[1]}")

print(dictionary)

dictionary["price"]=5000 # 추가
print(dictionary)

del dictionary["ingredient"]
print(dictionary)






