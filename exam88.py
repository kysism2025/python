class Animal:
    def __init__(self, age = 0):
        self.age = age

    def eat(self):
        print("동물이 먹고 있습니다.")

class Dog(Animal):
    def __init__(self, age = 0, name = ""):
        Animal.__init__(self, age)
        self.name = name

d = Dog(10, "해피")
print(d.age)

e = Animal(100)
print(e.age)