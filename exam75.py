'''
def create_student(name, korean, math, english, science):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

students=[
    create_student("윤인성", 87,98,88,95),
    create_student("연하진", 90,91,70,85),
    create_student("구지연", 90,70,78,65),
    create_student("나선주", 76,92,80,100),
    create_student("윤아린", 77,95,100,95),
    create_student("윤명월", 75,90,80,75)
]

print("이름","총점","평균", sep="\t")

for st in students:
    sum = (st["korean"]) + (st["math"]) + (st["english"]) + (st["science"])
    print(st["name"], sum, round(sum/len(students),1), sep="\t")
'''

def create_student(name, korean, math, english, science):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

def student_get_sum(st):
    return st["korean"] + st["math"]\
          + st["english"] + st["science"] 

def student_get_average(st):
    return round(student_get_sum(st) / 4, 1)

def student_to_string(st):
    return "{}\t{}\t{}".format(st["name"]\
                               ,student_get_sum(st),student_get_average(st))

students=[
    create_student("윤인성", 87,98,88,95),
    create_student("연하진", 90,91,70,85),
    create_student("구지연", 90,70,78,65),
    create_student("나선주", 76,92,80,100),
    create_student("윤아린", 77,95,100,95),
    create_student("윤명월", 75,90,80,75)
]

print("이름","총점","평균", sep="\t")

for st in students:
    print(student_to_string(st))

# 클래스 : 설계도
# 인스턴스 : 완성품
# 생성자 : 클래스 이름과 같음, 생성