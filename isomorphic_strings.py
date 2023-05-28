# https://leetcode.com/problems/isomorphic-strings/

# Conditions
# foo, bar
# f: b, a: o, r: o x
# bar, foo
# f: b, o: a, o: r x
# egg, add

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replaced = {}
        for i in range(len(s)):
            if (t[i] in replaced or 
            s[i] in replaced.values()) and replaced.get(t[i]) != s[i]:
                return False
            else:
                replaced[t[i]] = s[i]
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("bar", "foo"))