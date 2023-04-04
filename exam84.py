class Television:

    serialNumber = 0 # 클래스변수(공동사용)

    def __init__(self, channel, volume, on):
        self.__channel = channel
        self.__volume = volume
        self.__on = on
        #Television.serialNumber += 1        
        self.serialNumber += 1        
        self.__number = Television.serialNumber
        print("텔레비젼이 생성되었습니다.")

    def __del__(self):
        print("텔레비젼이 소멸되었습니다.")

    def __str__(self):
        print(f"{self.__channel},{self.__volume},{self.__on}")

    @classmethod
    def getSerialNumber(cls):
        return cls.serialNumber
    
    def show(self):
        print(self.__channel, self.__volume, self.__on, self.__number)
    

tv = Television(11, 10 ,True)
tv.show()
tv.show()
tv.show()

tv1 = Television(9, 2 , False)
tv1.show()
tv1.show()
tv1.show()

print("SN:", tv.serialNumber)
print("S/N:", Television.getSerialNumber())