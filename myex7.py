from myerror import myerror

'''
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a['age'] = 15
print(a.keys())
print(a.values())
print(a.items())
print(a.get('nokey','NONE'))
print('name' in a)
del a['name']
print(a)
a.clear()
print(a)
'''

try:
    #a = [1,2]
    #print(a[3])
    #4/0
    raise myerror.MyError()
except myerror.MyError as e:
    print(e) 
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")    
except IndexError:    
    print("인덱싱 할 수 없습니다.")
finally:
    print("작업을 종료하였습니다.")

    