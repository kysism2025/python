# items는 dict ==> for key, value in example_dictionary.items():

example_dictionary = {
    "키A":"값AAAA",
    "키B":"값BBBB",
    "키B":"값BBBB",
}

print("# 딕셔너리의 items()\n")
print("items():", example_dictionary.items())

for key, value in example_dictionary.items():
    print(f"{key}의 값은 {value}입니다.")

for key in example_dictionary:
    print(f"{key}의 값은 {example_dictionary[key]}")