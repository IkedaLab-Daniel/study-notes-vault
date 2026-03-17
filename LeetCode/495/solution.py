from typing import List

def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
        poison_duration = 0

        if len(timeSeries) == 1:
            return duration

        for i in range(1, len(timeSeries)):
            between = timeSeries[i] - timeSeries[i - 1]
            if between >= duration:
                poison_duration += duration
            else:
                poison_duration += between
        
        poison_duration += duration

        return poison_duration

print(findPoisonedDuration([1,2], 2))