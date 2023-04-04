# 함수 오버라이딩
# 생성자의 생성 시점


import math

# 자식 클래스의 함수가 부모 클래스의 함수를 오버라이드(재정의) 한다.

class Shape:
    def __init__(self): # 기본생성자  ==> 꼭 필요하지 않으면 작성 불필요!!! 초기값 설정 이외에는 불필요!!
        print("Shape를 생성했습니다.")

    def draw(self):
        print("Shape draw()가 호출됨!")

    def get_area(self):
        print("get_area()가 호출됨!")


class Circle(Shape):
    def __init__(self, radius = 0):
        # super().__init__() ==> # 시스템에서 자동으로 호출함 기본생성자 호출함
        self.radius = radius
        print("Circle을 생성했습니다.")

    def draw(self):
        super().draw()
        print("자식에서 draw()가 호출됨!")

    def get_area(self):
       return round(math.pi*self.radius**2,2)


circle = Circle() # 객체생성
circle.draw();    
print("원의면적1:", circle.get_area())


circle2 = Circle(10)
circle2.draw();    
print("원의면적2:", circle2.get_area())
