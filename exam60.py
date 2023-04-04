def call_n_times(n, func):
    for i in range(n):
        func()

def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")        


# 콜백함수
# call_10_times(print_hello)    
call_n_times(3, print_hello)


