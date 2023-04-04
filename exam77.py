class Counter:

    def __init__(self, count = 0) :
        self.__count = count
        print(self , "가 생성되었습니다.")
 
    def __del__(self) :
        print(self , "가 소멸되었습니다.")

    def increment(self):
        self.__count =+ 1

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        if value < 0:
            raise TypeError("count는 양의 숫자이어야 합니다.")
        self.__count = value


counter = Counter(0) # __init__(self) 호출
print("count::", counter.count)

#counter.increment()
counter.count = 100
print("count::", counter.count)

counter.count = 200
print("count::", counter.count)
    

        