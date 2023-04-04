example_list = ["요소A","요소B","요소C"]

print("#단순 출력")
print(example_list)
print()

print("# enumerate함수 적용 출력") # 현재 인덱스 몇번째인지 확인하고 싶을때 사용
print(enumerate(example_list))

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))

list_a = enumerate(example_list) # Tuple구조((인덱스1, 요소1), (인덱스2, 요소2).......)

print("반복문과 조합하기")    
for i, value in list_a:
    print(f"{i} 번째의 요소는 '{value}'입니다.")




