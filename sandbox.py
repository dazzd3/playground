import random as rd

class Rollnow:
    def rolld6(self):
        roll1 = rd.randint(1,6)
        roll2 = rd.randint(1,6)
        return roll1, roll2


dice = Rollnow()
print(Rollnow.rolld6)
