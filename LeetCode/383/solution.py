
def canConstruct(ransomNote: str, magazine: str) -> bool:
    for char in ransomNote:
        if char in magazine:
            magazine = magazine.replace(char, "", 1)
        else:
            return False
    return True


print(canConstruct("aa", "aab"))