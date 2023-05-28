# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            previous = row[0]
            for i in range(1, len(row)+1):
                if i < len(row):
                    row[i], previous = previous + row[i], row[i]
                elif i == len(row):
                    # print(row[0])
                    row.append(1)
        return row

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(1))