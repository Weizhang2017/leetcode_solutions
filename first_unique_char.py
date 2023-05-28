class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        dup = set()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                dup.add(s[i])
        if d:
            for k in d:
                if k not in dup:
                    return d[k]
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar('aabb'))