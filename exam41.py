i = 0

while True:
    print(f"{i}번째 반복문입니다.")
    i+=1

    input_text=input(">종료하시겠습니까?(y):")
    #if input_text == 'y': break
    if input_text in ["y","Y"]:
        break
    

