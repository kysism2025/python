def generator_func(x):
    print("첫번째 입력된 값 * 1:")
    x*=1
    yield x
    print("두번째 입력된 값 * 2:")
    x*=2
    yield x
    print("두번째 입력된 값 * 3:")
    x*=3
    yield x

#for i in generator_func(1):
#    print(i)

output = generator_func(1)

a = next(output)
print(a)

a = next(output)
print(a)

a = next(output)
print(a)