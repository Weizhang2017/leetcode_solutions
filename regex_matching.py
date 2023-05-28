# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        stack_s = []
        stack_p = []
        for i in s:
            stack_s.append(i)
        for pattern in p:
            stack_p.append(pattern)
        print(stack_p)
        print(stack_s)
        while stack_p and stack_s:
            pattern = stack_p.pop()
            if pattern == '*':


if __name__ == '__main__':
    s = Solution()
    s.isMatch("aa", 'a')
