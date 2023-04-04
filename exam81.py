class Student:

    title = "학생정보"

    def __init__(self, name = None, age = 0):
        self.__name = name  # __가 변수 앞에 붙으면 외부에서 변경(접근) 금지
        self.__age = age
        #print(f"학생정보 {self.__name}가 생성되었습니다")

    # def __del__(self):
    #     print(f"학생정보 {self.__name}가 소멸되었습니다")

    # def __str__(self):
    #     print(f"학생정보 => 이름:{self.__name} 나이:{self.__age}")
        
    # @classmethod
    # def printTitle(cls):
    #     print("타이틀 값 확인 : ", cls.title)

    # @property
    # def name(self):
    #     return self.__name
    
    # @name.setter
    # def name(self, value):
    #     self.__name = value

    # @property
    # def age(self):
    #     return self.__age
    
    # @age.setter
    # def age(self, value):
    #     if value <= 0 :
    #        print("나이가 잘못 입력되었습니다.")
    #        raise Exception
    #     self.__age = value

st = Student("Hong", 20)        
st.__age = 24
#print(st.name)
print(st.__age)
#print("None : ", type(None))

#Student.printTitle()
