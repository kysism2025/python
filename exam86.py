class Dog:
    kind="Bulldog"
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

a = Dog("Baduk", 2)
b = Dog("Merry", 3)

print(a.kind,a.name,a.age)
print(b.kind,b.name,b.age)

print(Dog.kind)



