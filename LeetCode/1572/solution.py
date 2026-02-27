from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
        length = len(mat[0])
        count = 0
        added = []

        if not length % 2 == 0:
            checkpoint = (length / 2) + 0.5

            for i in range(0, length):
                if i + 1 == int(checkpoint):
                    count += mat[i][i]
                    added.append(mat[i][i])
                    continue

                to_add = mat[i][i] + mat[i][-i - 1]
                count += to_add
                added.append([mat[i][i], mat[i][-i - 1]])
        else:
            for i in range(0, length):
                to_add = mat[i][i] + mat[i][-i - 1]
                count += to_add
                added.append([mat[i][i], mat[i][-i - 1]])
                 

        return count

mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]


print(diagonalSum(mat))