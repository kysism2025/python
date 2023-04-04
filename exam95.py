class MyTime:
    def __init__(self, hour, minute, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        #return f"시:분:초 ==> {self.hour}:{self.minute}:{self.second}"
        return "%.2d:%.2d:%.2d"%(self.hour,self.minute,self.second)

mytime = MyTime(1,10,10)
print(mytime)         