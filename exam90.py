import math

class Shape:
    # def __init__(self):  # 기본생성자  ==> 작성할 필요없으면 안써도 됨!!!
    #     pass

    def draw(self):
        print("draw()가 호출됨")

    def draw1(self):
        print("draw1111()가 호출됨")

    def get_area(self):
        print("get_area()가 호출됨")


class Circle(Shape):
    def __init__(self, radius=0):
        #super().__init__()
        self.radius = radius

    # 오바라이딩의 개념
    def draw(self):
        super().draw()
        print("원을 그립니다.")

    def get_area(self):
        super().get_area()
        return math.pi*self.radius**2
    

circle = Circle(10)    
circle.draw1()
circle.draw()
print(circle.get_area())

#shape = Shape()
#print(shape.get_area())

