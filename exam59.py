def swap(a, b):
    b, a = a, b
    return b, a

def test():
    return (10,20,30)

a, b = 10, 20
print("# 교환 이전 값")
print(f"a={a},b={b}")
print()

#b, a = a, b
b, a = swap(a, b)
print("# 교환 이후 값")
print(f"a={a},b={b}")
print()

a, b, c = test()
print(f"a={a},b={b},c={c}")