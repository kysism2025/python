class Employee:
    #name = "" # self의 name과 다름

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

    def getSalary(self):
        return self.salary
    

class Manager(Employee):
    def __init__(self, name="홍길동", salary=2000000, bonus=1000000):
        super().__init__(name, salary)
        self.bonus = bonus

    def getSalary(self):
        salary = super().getSalary() + self.bonus
        return salary
    
    def __str__(self):
        return f"이름:{self.name}\t월급:{self.getSalary()}\t보너스:{self.bonus}"
    
    def __repr__(self):
        return f"이름:{self.name}\t월급:{self.getSalary()}\t보너스:{self.bonus}"

kim = Manager("김철수", 3000000, 1000000)
#print("이름\t월급\t보너스")
#print(f"{kim.name}\t{kim.getSalary()}\t{kim.bonus}")
print(kim)

        