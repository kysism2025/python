class Student:

    __count = 0
    __students = []

    # 생성자 : 클래스 이름과 같은 함수, self : 자기자신(Student)
    def __init__(self, name, korean, math, english, science):
        # self.name = name
        # self.korean = korean
        # self.math = math
        # self.english = english
        # self.science = science
        self.__name = name
        self.__korean = korean
        self.__math = math
        self.__english = english
        self.__science = science        
        Student.__count += 1
        Student.__students.append(self)
        print("생성되었습니다.", Student.__count)

    def __str__(self):
        return "{}\t{}\t{}\t".format(self.__name, self.get_sum(),self.get_average())
    
    def __del__(self):
        print("파괴되었습니다.", Student.__count)
        Student.__count -= 1

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def korean(self):
        return self.__korean
    
    @korean.setter
    def korean(self, value):
        self.__korean = value

    @property
    def english(self):
        return self.__english
    
    @english.setter
    def english(self, value):
        self.__english = value
    
    @property
    def math(self):
        return self.__math
    
    @math.setter
    def math(self, value):
        self.__math = value

    @property
    def science(self):
        return self.__science
    
    @science.setter
    def science(self, value):
        self.__science = value

    def get_sum(self):
        return self.__korean + self.__math + self.__english + self.__science            

    def get_average(self):
        return round(self.get_sum() / 4, 1)

    @classmethod
    def print(cls):
        print("------ 학생목록 -----")
        print("이름\t총점\t평균")
        for student in cls.__students:
            print(str(student))
        print("--------------------")    
        
#students = [
Student("윤인성", 87,98,88,95)
Student("연하진", 90,91,70,85)
Student("구지연", 90,70,78,65)
Student("나선주", 76,92,80,100)
Student("윤아린", 77,95,100,95)
Student("윤명월", 75,90,80,75)
#]        

# students[0].name
# students[0].korean
# students[0].math
# students[0].english
# students[0].science

# for student in students:
#     print(str(student))
    
Student.print()

#Student.students[0].name
