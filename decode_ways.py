# https://leetcode.com/problems/decode-ways/

class Solution:
    counter = 0
    ways = []
    def numDecodings(self, s: str) -> int:
        
        nums = list(s)
        counter = 0
        if self.check(nums):
            counter += 1
        for i in s:
            if 0 < int(i) <=26:
                self.ways.append(i)
            else:
                j = self.ways.pop()
                if 0 < int(j+i) <= 26:
                    self.ways.append(j+i)
                else:
                    break
        return self.ways

    def check(self, nums, j):

        for i in nums:
            if i >= 26 or i == 0:
                return False
        return True



class Solution:
    def numDecodings(self, s: str) -> int:
        nums = []
        counter = 0
        if s[0] == '0':
            return counter
        else:
            nums.append(s[0])
        for i in range(1, len(s)):
            if s[i] != '0':
                nums.append(s[i])
            elif 0 < int(s[i-1:i+1]) <= 26:
                nums.pop()
                nums.append(s[i-1:i+1])
            else:
                return counter
        counter += 1
        for i in range(1, len(nums)):
            if len(nums[i]) == 1 and int(''.join(nums[i-1:i+1])) <= 26:
                counter += 1
            else:
                print('test')
                continue
            for j in range(i+1, len(nums)-1):
                if len(nums[j]) == 1 and int(''.join(nums[j:j+2])) <= 26:
                    counter += 1
        return counter


            
        # for i in range(len)
from functools import lru_cache

class Solution:  # 36 ms, faster than 34.07%
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(i):
            if i == len(s): return 1
            ans = 0
            if s[i] != '0':  # Single digit
                ans += dp(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):  # Two digits
                ans += dp(i + 2)
            return ans

        return dp(0)

if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("111111111111111111111111111111111111111111111"))
