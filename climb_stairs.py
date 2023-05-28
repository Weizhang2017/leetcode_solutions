#https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        m = [0] * (n + 1)
        m[0] = m[1] = 1
        for i in range(2, n+1):
            m[i] = m[i-2]+m[i-1]
        print(m)
        return m[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(6))