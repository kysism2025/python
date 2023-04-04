class Car:
    def __init__(self, speed, color, model):
        self.__speed = speed
        self.__color = color
        self.__model = model
        print(f"자동차 {self.__model} 객체를 생성하였습니다.")

    def __del__(self):
        print(f"자동차 {self.__model} 객체가 소멸되었습니다.")

    def __str__(self):
        print(f"차량정보 => 속도:{self.speed}, 컬러:{self.color}, 모델명:{self.model}")

    def drive(self):
        self.speed = 60

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value    

myCar = Car(0, "blue", "Tusan")    

print(f"자동차의 속도 : {myCar.speed}")
print(f"자동차의 컬러 : {myCar.color}")
print(f"자동차의 모델 : {myCar.model}")