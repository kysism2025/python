'''
try:
    예외가 발생할 가능성이 있는 구문
except 예외의 종류 as 예외 객체를 활용할 변수 이름 :
    예외가 발생했을때 실행할 구문
else:
    예외가 발생하지 않았을때 실행할 구문
finally:
    마지막으로 무조건 실행할 구문

예외의 종류

SyntaxError
NameError
IndexError
ValueError
FileNotFoundError
TypeError
AttributeError
KeyError
등
'''

try:
    number_input_a = int(input("정수입력>"))
    print("원의 반지름",number_input_a)
    print("원의 둘레:",2*3.14*number_input_a)
    print("원의 넓이:",3.14*number_input_a*number_input_a)
except ValueError as e:
    print("정수를 입력하세요~~")
    print("type(exception):", type(e))
    print("exception:", e)
except Exception as e:    
    print("type(exception):", type(e))
    print("exception:", e)
else:
    print("오류가 발생하지 않았습니다.")
finally:
    print("마지막으로 실행하였습니다.")    

