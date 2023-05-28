# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        i = 0
        for _s in s:
            while i < len(t) and _s != t[i]:
                i += 1
            if i >= len(t):
                return False
            i += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "acb"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))

