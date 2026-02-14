from typing import List


def rob(nums: List[int], colors: List[int]) -> int:
    result = 0
    i = 0
    while True:
        if i == len(nums) - 1:
            break
        
        if colors[i] == colors[i + 1]:
            if nums[i] > nums[i + 1]:
                nums.pop(i + 1)
                colors.pop(i + 1)
                continue
            else:
                nums.pop(i)
                colors.pop(i)
                continue
        i += 1

    print(nums)
    print(colors)
    return result

print(rob(nums=[1,4,3,5], colors=[1,1,2,2]))