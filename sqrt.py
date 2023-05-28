#https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        for i in range(x+1):
            if i ** 2 > x:
                return i-1

    def mySqrt2(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        n = x // 2
        upper = n
        lower = 0
        if n ** 2 <= x:
            return n
        while upper - lower > 1:
            n = (lower + upper) // 2
            if n ** 2 == x:
                return n
            if n ** 2 > x:
                upper = n
            else:
                lower = n
        return lower

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt2(8))