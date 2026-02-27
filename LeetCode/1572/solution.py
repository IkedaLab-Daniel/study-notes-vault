from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
        length = len(mat[0])
        count = 0

        if length == 1:
            return mat[0][0]

        if not length % 2 == 0:
            checkpoint = (length / 2) + 0.5

            for i in range(0, length):
                to_add = mat[i][i] + mat[i][-i - 1]
                count += to_add
            
            return count - mat[int(checkpoint) - 1][int(checkpoint) - 1]

        else:
            for i in range(0, length):
                to_add = mat[i][i] + mat[i][-i - 1]
                count += to_add

        return count

mat = [[1,2,3],[4,5,6],[7,8,9]]


print(diagonalSum(mat))