from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "C":
                record = record[:len(record) - 1]
            elif op == "D":
                double_prev = record[len(record) - 1] * 2
                # record = record[:len(record) - 1]
                record.append(double_prev)
            elif op == "+":
                to_add = record[len(record) - 2] + record[len(record) - 1]
                record.append(to_add)
            else:
                record.append(int(op))
        
        count = 0
        for num in record:
            count = count + num
        
        return count

ICE = Solution()
# print(ICE.calPoints(["5","2","C","D","+"]))
# print(ICE.calPoints(["1", "C"]))
print(ICE.calPoints(["5","-2","4","C","D","9","+","+"]))