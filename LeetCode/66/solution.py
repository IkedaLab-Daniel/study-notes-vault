from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = "".join(map(str, digits))
        new = int(str_digits) + 1
        final = []
        for num in str(new):
            final.append(int(num))
        
        return final
        
ICE = Solution()
print(ICE.plusOne([1,2,3,4]))