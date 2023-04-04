class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 init메소드가 호출되었습니다.")

    def test(self):
        print("Parent 클래스의 test메소드가 호출되었습니다.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child 클래스의 init메소드가 호출되었습니다.")

class CustomerException(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.__message = message
        self.__value = value

    def __str__(self):
        return "CustomerException오류가 발생하였습니다. "
    
    def print(self):
        print("==== 오류 정보 ====")
        print("메시지:", self.__message)
        print("값:", self.__value)
        

child = Child()
child.test()

print(child.value)

try:
    raise CustomerException("테스트 오류발생", 99)
except Exception as e:
    print(e)
    print(e.print())


schools = ["A School","A School","B School","C School","C School","D School","D School"]    

set = set()

for school in schools:
    set.add(school)

list(set).sort()

print(f"{len(set)}개 학교:{set}")    