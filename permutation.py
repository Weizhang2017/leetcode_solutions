'''
procedure generate(n : integer, A : array of any):
    if n = 1 then
          output(A)
    else
        for i := 0; i < n; i += 1 do
            generate(n - 1, A)
            if n is even then
                swap(A[i], A[n-1])
            else
                swap(A[0], A[n-1])
            end if
        end for
    end if
'''
# https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.l = []
        self._permute(nums, len(nums))
        return self.l

    def _permute(self, nums, n):
        if n == 1:
            self.l.append(list(nums))
        else:
            for i in range(n):
                self._permute(nums, n-1)
                if n % 2 == 0:
                    nums[i], nums[n-1] = nums[n-1], nums[i]
                else:
                    nums[0], nums[n-1] = nums[n-1], nums[0]
        return self.l

if __name__ == '__main__':
    s = Solution()
    nums = [0,1]
    n = len(nums)
    print(s.permute(nums))