numbers = [273,103,5,32,65,9,72,800,99]
'''
# for, if 사용 100이상의 숫자
for item in numbers:
    if item >= 100:
        print(item)


for item in numbers:
    if item % 2 == 0:
        print("{}는 짝수입니다.".format(item))
    else:
        print("{}는 홀수입니다.".format(item))
'''

import enum

class DigitRank(enum.Enum) :
        D_ONE = 0
        D_TWO = 1
        D_THREE = 2
        D_FOUR = 3
    
a = DigitRank.D_ONE    
print(a.name)    
print(a.value)    
print(DigitRank.D_ONE.value)   
    
'''
# 숫자 길이(자리수) 계산        
for item in numbers:
    if item // 1000 > 0:
       print("{}는 네자리 입니다.".format(item))
    elif item // 100 > 0:
       print("{}는 세자리 입니다.".format(item))
    elif item // 10 > 0:
        print("{}는 두자리 입니다.".format(item))
    else:
        print("{}는 한자리 입니다.".format(item))

for item in numbers:
    print("{}는 {}자리 입니다.".format(item,len(str(item))))
'''        