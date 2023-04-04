# format() 함수로 숫자를 문자열로 변환

string_a = "{}".format(10)

print(string_a)
print(type(string_a))

format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
format_c = "{} {} {}".format(3000,4000,5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

output_a = "{:d}".format(52)
print("# 기본")
print(output_a)

output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
print("# 특정칸에 출력하기")
print(output_b)
print(output_c)

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

output_f = "{:=+5d}".format(52) # 기호를 앞으로 밀기 : 양수
output_g = "{:=+5d}".format(-52) # 기호를 앞으로 밀기 : 음수
print(output_f)
print(output_g)

output_h="{:f}".format(52.273)
output_i="{:15f}".format(52.273)   # 15칸 만들기
output_j="{:+15f}".format(52.273)  # 15칸에 부호 추가하기
output_k="{:+015f}".format(52.273) # 15칸에 부호 추가하고 0으로 채우기
print(output_h)
print(output_i)
print(output_j)
print(output_k)

output_l="{:15.3f}".format(52.273)
output_m="{:15.2f}".format(52.273)
output_n="{:15.1f}".format(52.273)
print(output_l)
print(output_m)
print(output_n)

output_o=52.0
output_b="{:g}".format(output_o) # 의미없는 소수점 없애기
print(output_o)
print(output_b)






