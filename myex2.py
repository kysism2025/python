# class 부모클래스:
# class 자식클래스(부모클래스):

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_name(self):
    return self.name
    
  def get_age(self):
    return self.age
    
class Student(Person):
  def __init__(self, name, age, grade):
    super().__init__(name, age)
    self.grade = grade

  def get_grade(self):
    return self.grade
   
a = Student('Dave', 27, 'A')
b = Student('Tom', 32, 'B')
 
print(f'{a.get_name()} is {a.get_age()} years old and grade is {a.get_grade()}')
print(f'{b.get_name()} is {b.get_age()} years old and grade is {b.get_grade()}')

# Dave is 27 years old and grade is A
# Tom is 32 years old and grade is B