class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_p = s[0]
        for i in range(n-1):
            p = s[i]
            max_j = min(i, n-i-1)
            for j in range(1, max_j+1):
                if s[i-j] != s[i+j]:
                    # p = s[i-j+1:i+j]
                    break
                else:
                    p = s[i-j:i+j+1]
            if len(p) > len(max_p):
                max_p = p
            if s[i] == s[i+1]:
                p = s[i:i+2]
                max_j = min(i, n-i-2)
                for j in range(1, max_j+1):
                    if s[i-j] != s[i+j+1]:
                        # p = s[i-j+1:i+j+1]
                        break
                    else:
                        p = s[i-j:i+j+2]
            if len(p) > len(max_p):
                max_p = p
        return max_p

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('cabbac'))