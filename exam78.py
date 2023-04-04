class Television:

    def __init__(self, channel, volumn, power):
        self.__channel = channel
        self.__volumn = volumn
        self.__power = power

    def __del__(self):
        print("소멸되었습니다.")

    def show(self):
        print("{}\t{}\t{}".format(self.__channel, self.__volumn, self.__power))

    @property
    def channel(self):
        return self.__channel
    
    @channel.setter
    def channel(self, value):
        if value < 0:
            raise TypeError("count는 양의 숫자이어야 합니다.")
        self.__channel= value

    @property
    def volumn(self):
        return self.__channelvolumn
    
    @volumn.setter
    def volumn(self, value):
        if value < 0:
            raise TypeError("volumn은 양의 숫자이어야 합니다.")
        self.__volumn = value

    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, value):
        self.__power = value                


    
tv = Television(11, 3, "ON")    
print(tv.show())

tv.channel = 9
print(tv.show())

print("현재 선택한 채널:", tv.channel)