# raise : 의도적으로 에러를 발생시켜야 하는 경우
# 상위 클래스를 설계 할때  하위 클래스에서 반드시 오버라이드 하여
# 상세하게 구현해야 하는 함수를 명시하고자 하려면 해당 함수의 내용으로
# raise NotImplementedError(메시지)로 처리한다.

import math

class Shape:
    def __init__(self, name):
        self.name = name
        
    def getArea(self):
        raise NotImplementedError("이것은 추상함수 입니다.")
        #추상함수 : 내용이 없는 함수


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius**2
        #print("Circle함수의 getArea를 호출하였습니다.")


class Rectangle(Shape):
    def __init__(self, name, width=2, height=1):
        super().__init__(name)
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height


# lst = []
# shape = Shape("홍길동")
# circle = Circle("이길동", 3)
# rectangle = Rectangle(30)

# lst.append(circle)
# #lst.append(rectangle)

# for st in lst:
#  print(st.getArea())

# try:
#     #shape.getArea()
#     #print(round(circle.getArea(),2))
#     #print(round(rectangle.getArea(),1))
#     pass

# except NotImplementedError as e:
#     print(e)    

# except Exception as e:
#     print(e)

# finally:
#     print("마지막으로 처리하였습니다.")


