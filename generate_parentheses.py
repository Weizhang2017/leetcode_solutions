# https://leetcode.com/problems/generate-parentheses/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        # dp[0] = ''
        for i in range(n):
            for j in range(n-i):
                for k in range(n-i-j):
                    l.append('()' * i + '(' * (j + 1) + '()' * k + ')' * (j + 1) + '()' * (n - j - 1 - i - k))
        return set(l)

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(4))