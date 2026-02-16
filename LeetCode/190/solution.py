class Solution:
    def reverseBits(self, n: int) -> int:
        binary = str(bin(n))[2:]
        to_add = 32 - len(binary)
        expanded = (to_add * "0") + binary
        reverse = int(expanded[::-1], 2)

        return reverse