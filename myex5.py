# from mod1 import add
import mod1

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
         if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
             return 0
         else:
             return self.first / self.second

class Family:
    lastname = "김"

a =  MoreFourCal(10,20)
print(a.pow())
print(a.add())

b = SafeFourCal(20,10)
print(b.div())

# mod1.py의 add함수 사용하기
#print(add(1,2))  # from mod1 import add인 경우만 허용됨
print(mod1.add(3,5)) # import mod1인 경우만 허용