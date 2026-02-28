from typing import List

def average(salary: List[int]) -> float:
        highest = max(salary)
        lowest = min(salary)
        n = len(salary)

        total = sum(salary)
        reduced = total - highest - lowest

        average = reduced / (n - 2)

        return average

result = average(salary=[1000,2000,3000])
print(result)