numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)

#print("reversed_numbers :", r_num)
#print(list(r_num))

# 반복할 수 있을 때는 해당 값을 출력하고, 반복이 끝났을 때는 기본값을 출력합니다
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))


# iterable 객체에 있는 iterator
numbers = [1,2,3,4,5,6]
numbers = iter(numbers)

while True:
    tmp = next(numbers, None)
    if tmp is None:
        break
    print(tmp)

example_dictionary = {
    "키A":"값AAAA",
    "키B":"값BBBB",
    "키C":"값CCC",
}    
exiter= iter(example_dictionary)

while True:
    tmp = next(exiter, None)
    if tmp is None:
        break
    print(f"{tmp}:{example_dictionary[tmp]}")


