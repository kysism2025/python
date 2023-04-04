class Animal():
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"개의 이름은 {self.name}입니다"
        
class Person():
    def __init__(self, name):
        self.name = name
        self.pet = None

    def __str__(self):
        if self.pet != None:
            return f"나의 이름은 {self.name}이고 기르는 애완동물의 이름은 {(self.pet).name}입니다."   
        else:
            return f"나의 이름은 {self.name}이고 기르는 애완동물은 기르지 않습니다."   

dog = Dog("멍멍이") 
print(dog)       

person = Person("홍길동")
person.pet = dog
print(person)

person2 = Person("최길동")
print(person2)