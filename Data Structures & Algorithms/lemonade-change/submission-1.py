class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                if fives == 0:
                    return False
                else:
                    tens += 1
                    fives -= 1
            elif i == 20:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                    twenties += 1
                elif fives >= 3:
                    fives -= 3
                    twenties += 1
                else:
                    return False
        return True