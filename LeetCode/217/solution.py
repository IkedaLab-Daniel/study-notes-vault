from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)

        if len(nums) == len(set_num):
            return False
        
        return True