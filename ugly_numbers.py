# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1:
            found = False
            for factor in [2, 3, 5]:
                if n % factor == 0:
                    n //= factor
                    found = True
            if not found:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(1))