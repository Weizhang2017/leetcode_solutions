# https://leetcode.com/problems/pascals-triangle/
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = []
        for n in range(numRows):
            l.append([])
            for i in range(n+1):
                if n - 1 >= 0:
                    if i - 1 >= 0:
                        if i < n:
                            l[n].append(l[n-1][i-1] + l[n-1][i])
                        else:
                            l[n].append(l[n-1][n-1])
                    else:
                        l[n].append(l[n-1][i])
                else:
                    l[n].append(1)
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.generate(4))