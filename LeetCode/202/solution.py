def isHappy(self, n: int) -> bool:
        seen = set()

        while not n == 1:
            if n in seen:
                return False
            seen.add(n)

            str_n = str(n)
            digits = len(str_n)
            count = 0

            for i in range(0, digits):
                val = int(str_n[i])
                num = val ** 2
                count += num

            n = count

        return True

print(isHappy(19))