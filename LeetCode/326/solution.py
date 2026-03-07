def isPowerOfThree(n: int) -> bool:
        for i in range(1, int(n / 3) + 1):
            if i**3 == n:
                return True

        return False

print(isPowerOfThree(9))