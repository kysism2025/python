# lambda 매개변수 : 리턴값

power = lambda x : x * x
under_3 = lambda x : x < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print("#map()함수 실행 결과")
#print(output_a)
#print(list(output_a)) # [1, 4, 9, 16, 25]

output_b = map(under_3, list_input_a)
#print(output_b)
#print(list(output_b)) # [True, True, False, False, False]

output_c = map(lambda x : x + x, list_input_a)
print(list(output_c))

output_d = map(lambda x : x < 4, list_input_a)
print(list(output_d))