# yield : 함수내부의 코드가 실행되지 않음
def test():
    print("A지점 통과")
    yield 1 # return 1
    print("B지점 통과")
    yield 2 # return 2
    print("C지점 통과")

output = test()
while True:
  try:
    a = next(output)
    if a:
        print(a)
    else:
        break
  except StopIteration:
     break
  

# print("D지점 통과")
# a = next(output)
# print(a)

# print("E지점 통과")
# a = next(output)
# print(a)