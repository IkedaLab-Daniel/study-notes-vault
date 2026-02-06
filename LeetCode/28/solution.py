class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_start = needle[0]

        for i in range(0, len(haystack)):
            if needle_start == haystack[i]:
                if needle == haystack[i : (i + len(needle))]:
                    return i
        
        return -1
    
ice = Solution()
result = ice.strStr("sadbutsad", "sad")
print(f"\033[92m")
print(result)