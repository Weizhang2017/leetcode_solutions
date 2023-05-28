# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for i in range(len(strs)):
            d = {}
            for letter in strs[i]:
                d[letter] = d.get(letter, 0) + 1
            s = set()
            for key, value in d.items():
                s.add((key, value))
            fs = frozenset(s)
            l[fs].append(strs[i])
        return list(l.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1
            d[tuple(count)].append(s)
        return list(d.values())



if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))