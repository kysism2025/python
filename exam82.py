class Student:

    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age
        print(f"학생정보 {self.__name}가 생성되었습니다")

    def __del__(self):
        print(f"학생정보 {self.__name}가 소멸되었습니다")

    def __str__(self):
        print(f"학생정보 => 이름:{self.__name} 나이:{self.__age}")
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value <= 0 :
           print("나이가 잘못 입력되었습니다.")
           raise Exception
        self.__age = value



