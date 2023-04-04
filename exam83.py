class Television:
    
    def __init__(self, channel, volume, on):
        self.__channel = channel
        self.__volume = volume
        self.__on = on
        print("텔레비젼이 생성되었습니다.")

    def __del__(self):
        print("텔레비젼이 소멸되었습니다.")

    def __str__(self):
        print(f"{self.__channel},{self.__volume},{self.__on}")

    @property
    def channel(self):
        return self.__channel
    
    @channel.setter
    def channel(self, value):
        self.__channel = value

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def on(self):
        return self.__on
    
    @on.setter
    def on(self, value):
        self.__on = value        


def setSilentMode(t):
    t.volume = 2


myTv = Television(11, 10, True)        


setSilentMode(myTv)


print(myTv.volume)
