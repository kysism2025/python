tupleVariable = (10, 20, 30)
tupleVariable2 = (10, "A", "C")
tupleVariable3 = ("영희", "철수", 30)  # 튜플 선언 및 초기화

print(tupleVariable)  # 튜플 내용 확인
print(tupleVariable[0])  # tupleVariable 0번째 index 가져오기(0부터 시작)
print(tupleVariable.index(20))  # 튜플 안에 20이 몇번째 index에 있는지 확인
print(3 in tupleVariable)  # 튜플 안에 3이 들어있는지 확인
print(len(tupleVariable))  # 튜플 length 확인
print(sum(tupleVariable))  # 튜플 안의 값 모두 더하기