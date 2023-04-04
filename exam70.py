list_input_a = ["52","273","32","스파이","103"]
list_number = []

for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass
    else:
        print("예외가 발생하지 않았을 때 실행할 코드")
    finally:
        print("finally는 예외무관 무조건 실행")

print("{}내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

