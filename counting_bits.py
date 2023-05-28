# https://leetcode.com/problems/counting-bits/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            sum_ = 0
            while i:
                sum_ += i % 2
                i //= 2
            l.append(sum_)
        return l

if __name__ == '__main__':
    n = 1
    s = Solution()
    print(s.countBits(n))