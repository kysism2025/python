'''
number = int(input("정수 입력>"))

if number % 2 == 0:
    print(("입력한 문자열은 {}입니다.\n"
"{}는(은) 짝수입니다.").format(number, number))
else:
    print(("입력한 문자열은 {}입니다.\n"
"{}는(은) 홀수입니다.").format(number, number))
'''

print("::".join(["1","2","3","4","5"]))

number = int(input("정수 입력>"))

if number % 2 == 0:
    print("\n".join(["입력한 문자열은 {}입니다.",
"{}는(은) 짝수입니다."]).format(number, number))
else:
    print("\n".join(["입력한 문자열은 {}입니다.",
"{}는(은) 홀수입니다."]).format(number, number))