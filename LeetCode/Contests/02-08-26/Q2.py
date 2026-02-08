from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        updated = nums[:]
        again = False
        while True:
            again = False
            for i in range(0, len(updated) - 1):
                if (updated[i] == updated[i + 1]):
                    to_add = updated[i] * 2
                    updated.pop(i)
                    updated.pop(i)
                    updated.insert(i, to_add)
                    again = True
                    break
            if not again:
                return updated

ICE = Solution()
print(ICE.mergeAdjacent([2, 2, 4]))