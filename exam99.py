import random

class Dice:
    def __init__(self):
        self.__sides_count = 6

    def get_sides_count(self):
        return self.__sides_count
    
    def roll(self):
        # random 0.0 <= x < 1.0 ==> 0.00000 ~ 0.999999....
        return random.randint(1, self.__sides_count)
    

class FraudDice(Dice):
    def __init__(self):
        super().__init__()

    def roll(self):
        while True:
            self.r = super().roll()
            if self.r > 3:
                return self.r
                
    def __str__(self):
        return f"{self.roll()}"

dice = FraudDice()
print(dice)