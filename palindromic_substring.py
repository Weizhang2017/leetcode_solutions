class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        counter = 0
        for i in range(n-1):
            max_j = min(i, n-i-1)
            counter += 1
            for j in range(1, max_j+1):
                if s[i-j] == s[i+j]:
                    counter += 1
                else:
                    break
            if s[i] == s[i+1]:
                counter += 1
                max_j = min(i, n-i-2)
                for j in range(1, max_j+1):
                    if s[i-j] == s[i+j+1]:
                        counter += 1
                    else:
                        break
        return counter + 1

if __name__ == '__main__':
    s = Solution()
    s_ = "aaa"
    print(s.countSubstrings(s_))