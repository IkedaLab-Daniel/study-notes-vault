from typing import List

def lemonadeChange(bills: List[int]) -> bool:
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five:
                    five -= 1
                else:
                    return False
            elif bill == 20:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True

result = lemonadeChange([5,5,10,10,20])
print(result)