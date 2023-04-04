# 1*99, 2*99, 3*97 ..... 98*2, 99*1 최대값이 되는 경우 어떤 숫자?

max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    if max_value < i*j:
      a = i
      b = j
      max_value = a*b


print(f"최대값 : {a}*{b} = {max_value}")