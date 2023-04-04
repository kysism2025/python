def fx1():
    print("fx1...")


def fx2(a):
    print("fx2..", a)


def fx3(a, b):
    print("fx3...", a, b)


def fx4(a=3, b=4):
    print("fx4..", a, b)


def fx5(a, b, c=11, d=33):
    print("fx5..", a, b, c, d)


def fx6(a, b_list):
    print("fx6..", a)
    for x in b_list:
        print(x)


ff2 = []


def add_callback(callback, *args, **kw):
    # print(myfx, args, kw)
    ff2.append((callback, args, kw))


def run_fx2(ff):
    # print("ff2 = ", ff)
    for callback, arg, kw in ff:
        callback(*arg, **kw)


add_callback(fx1)
add_callback(fx4, 93)
add_callback(fx4, 93, b=777)
add_callback(fx5, 91, 92, c=93, d=94)
add_callback(fx6, 11, [100, 101, 102])

run_fx2(ff2)