# 가장 저렴한 책과 비싼책 구하기

books = [{
    "제목" : "혼자공부하는파이썬",
    "가격" : 18000
},{
    "제목" : "혼자공부하는 머신러닝",
    "가격" : 20000
},{
    "제목" : "혼자공부하는 C언어",
    "가격" : 11000
}
]



print("===오름차순===")
books.sort(key=lambda bok:bok["가격"])
for contents in books:
    print("{}:{}".format(contents["제목"],contents["가격"]))

print()
print("===내림차순===")
books.sort(reverse=True, key=lambda bok:bok["가격"])    
for contents in books:
    print("{}:{}".format(contents["제목"],contents["가격"]))

'''
# lambda : 함수를 대신하여 사용
# lambda형식 : lambda 매개변수: return값
print("가장 싼 책")
#print(min(books, key=getPrice))
print(min(books, key=lambda book:book["가격"]))
print()
print("가장 비싼 책")
#print(max(books, key=getPrice))
print(max(books, key=lambda book:book["가격"]))
'''

# max_content = {}
# min_content = {}
# max_price = 0
# i = 0
# for contents in books:
#     if i is 0:
#        max_price = int(contents["가격"])
#        min_price = int(contents["가격"])
#     else:   
#         if contents["가격"] > max_price:
#             max_content = contents
#         if contents["가격"] < min_price:
#             min_content = contents
#     i += 1    

# print("가장비싼책 ==> {}:{}".format(max_content["제목"],max_content["가격"]))
# print("가장싼책 ==> {}:{}".format(min_content["제목"],min_content["가격"]))
