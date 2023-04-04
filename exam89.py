class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

class Student:
    def  __init__(self, id):
        self.id = id

    def getId(self):
        return self.id
    
# 다중상속 개념    
class CollegtStudent(Person, Student):
    def  __init__(self, name, age, id):
        Person.__init__(self, name, age) # 클래스명으로 init를 호출시 self 인수를 반드시 넣어준다.
        Student.__init__(self, id)

    def descAll(self):
        print(f"{self.name},{self.age},{self.id}")    

    
cs = CollegtStudent("안철수", 10, "an")
cs.descAll()