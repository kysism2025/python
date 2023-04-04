import math

class Circle:
    def __init__(self, radius = 0):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__radius = value

    def getArea(self):
        return math.pi * self.radius * self.radius

    def gerPerimeter(self):
        return 2*math.pi*self.radius

circle = Circle(10)

print(f"원의 면적:{round(circle.getArea(),1)}")
print(f"원의 둘레:{round(circle.gerPerimeter(),1)}")