# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if digits == "":
#             return ""

#         m = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#         global vis
#         vis = {}
#         for digit in digits:
#             for i in m[digit]:
#                 vis[i] = vis.get(i, 0) + 1
#         if len(digits) == 1:
#             return list(m[digits])
#         AL = {}
#         global l
#         l = []
#         for i in range(1, len(digits)):
#             for letter in m[digits[i-1]]:
#                 AL[letter] = list(m[digits[i]])
#         print(AL)
#         for letter in m[digits[0]]:
#             self.dfs(letter, AL)
#         return l

#     def dfs(self, u, AL):
#         if AL.get(u) and vis[u] > 0:
#             vis[u] -= 1
#             for v in AL[u]:
#                 print(v)
#                 self.dfs(v, AL)
#                 # l.append(u + self.dfs(v, AL))
#         else:
#             return u


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return ""

        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        l = []
        for i in digits[::-1]:
            l.append(list(m[i]))

        new_l = l.pop()
        final_l = new_l
        while l:
            l_ = l.pop()
            final_l = []
            for i in new_l:
                for j in l_:
                    final_l.append(i+j)
            new_l = final_l
        return final_l

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('2'))
