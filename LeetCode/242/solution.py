class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = sorted(s)
        new_t = sorted(t)

        if not len(s) == len(t):
            return False

        for i in range(0, len(s)):
            if not new_s[i] == new_t[i]:
                return False
        
        return True
            

ICE = Solution()
print(ICE.isAnagram("anagram", "nagaram"))