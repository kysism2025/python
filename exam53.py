# 함수
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

def print_n_times(value, n):
    for i in range(n):
        print(value)

def print_n_values(n, *values): # 가변 매개변수
    for value in values:
        print(value)
    print()

def print_n_values2(value, n=2):
    for i in range(n):
        print(value)

def print_n_values3(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

def return_test():
    print("A위치입니다.")
    return
    print("B위치입니다.")

def sum_all(start=0, end=100, step=1):
    output = 0

    for i in range(start, end+1, step):
        output += i
    return output        


#print_3_times()
#print_n_times('안녕하세요', 5)
#print_n_values(3, "안녕하세요","즐거운","파이썬 프로그래밍")
#print_n_values2('기본횟수만 반복')
#print_n_values2('5회반복', 5)
#print_n_values3("안녕하세요","즐거운","파이썬 프로그래밍", n=3) # n이라는 변수를 반드시 명시해야 매개변수로 인식

#value = return_test()
#print(value) # None

print("sum_all", sum_all())
print("sum_all", sum_all(10))  # 순서대로 인식됨
print("sum_all", sum_all(start=50))
print("sum_all", sum_all(start=50, step=5, end=200)) # 이름으로 명시됨