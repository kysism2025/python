class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make
    

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        Car.__init__(self, make, model, color, price) # super()로 호출시에는 self를 인수로 넣지 않는다.
        self.batterySize = batterySize

    def setBatterySize(self, batterySize):
        self.batterySize = batterySize

    def getBatterySize(self):
        return self.batterySize
    
    def getDesc(self):
        return f"차량=({self.make},\
                    {self.model},\
                    {self.color},\
                    {self.price},\
                    {self.batterySize})"


def main():
    car = ElectricCar('현대','Tusan',"검정", 2000, 300)
    car.setMake("기아")
    car.setBatterySize(60)
    print(car.getDesc())


main()    