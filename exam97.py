class Person:
    def __init__(self):
         print("첫번째 생성자 호출")

    def __init__(self, name, number):
        self.name = name
        self.number = number

class Student(Person):        
    UNDERGRADUATE=0
    POSTGRADUATE=1

    def __init__(self, name, number, studentType):
        #super().__init__(name, number)
        self.studentType = studentType
        self.gpa = 0
        self.classes = []

    def __str__(self):
        return f"\n이름={self.name}\n주민번호={self.number}\n수강과목={self.classes}\n평점={self.gpa}"
    
    def enrollCourse(self, course):
        self.classes.append(course)

    def __repr__(self):
        pass


class  Teacher(Person):
    def __init__(self, name, number):
        #super().__init__(name, number)
        self.courses = []
        self.salary = 3000000

    def assignTeaching(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"\n이름={self.name}\n주민번호={self.number}\n강의과목={self.courses}\n월급={self.salary}"

st1 = Student("홍길동", "12345678", Student.UNDERGRADUATE)
st1.enrollCourse("자료구조")
print(st1)

te1 = Teacher("김철수", "1234567890")
te1.assignTeaching("Python")
#print(te1)



