class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_list = s.split(" ")
        print(new_list)

        ice = 0
        while True:
            if new_list[len(new_list) - 1 - ice] == '':
                ice = ice + 1
                continue

            return len(new_list[len(new_list) - 1 - ice])
        
ICE = Solution()
print(ICE.lengthOfLastWord("   fly me   to   the moon  "))