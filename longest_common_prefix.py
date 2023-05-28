from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        i = 0
        stop = False
        while i < len(strs[0]):
            for ind in range(1,len(strs)):
                if len(strs[ind-1]) <= i or len(strs[ind]) <= i or strs[ind-1][i] != strs[ind][i]:
                    stop = True
                    break
            if stop:
                break
            i += 1
        return strs[0][:i]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flower","flower","flower"]))