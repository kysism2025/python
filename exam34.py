character = {
    "name":"기사",
    "level": 12,
    "items": {
         "sword": "불꽃의 검",
         "armor": "풀플레이트"
    },
    "skill": ["베기","세게 베기","아주 세게 베기"]
}

'''
print(character)
print(character["items"]["sword"])
print(type(11) is int)
print(type("문자열") is str)
print(type([]) is list)
print(type({}) is dict)

for ch in character:
    print(ch)
'''

for key in character:
    if type(character[key]) is list:
        for item in character[key]:
            print(f"{key}:{item}")
    elif type(character[key]) is dict:
        for smallkey in character[key]:
            print(f"{smallkey}:{character[key][smallkey]}")
    else:
        print(f"{key}:{character[key]}")
