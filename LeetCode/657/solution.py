class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = 0
        vertical = 0

        for move in moves:
            if move == "U":
                horizontal += 1
            elif move == "D":
                horizontal -= 1
            elif move == "R":
                vertical += 1
            else:
                vertical -= 1
        
        if abs(horizontal) + abs(vertical) == 0:
            return True
        return False