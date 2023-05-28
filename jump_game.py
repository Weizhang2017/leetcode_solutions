from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        step_back = 1
        step0 = 0
        step_back_found = False
        while i < n - 1:
            if nums[i] != 0:
                i = i + nums[i]
                
                if i > step0:
                    step_back = 1
            elif i - step_back >= 0:
                step0 = max(i, step0)
                i -= step_back
                count = 1
                while i + nums[i] <= step0 and i - step_back >= 0:
                    i -= step_back
                step_back += count
            else:
                return False

        return i >= n - 1

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,3,2,3,1,1,3,2,3,3,3,2,2,3,1,1,2,2,3,3,2,3,3,3,2,2,2,1,1,3,2,1,2,1,2,2,2,1,3,3,2,2,2,1,1,3,1,1,2,1,3,1,2,3,1,2,1,3,3,2,2,2,1,1,3,3,2,1,2,3,2,1,2,2,1,3,2,2,3,1,2,1,3,1,1,2,2,1,3,2,3,2,1,2,2,2,2,1,2,1,2,1,3,2,2,3,3,1,2,2,3,1,3,2,3,2,2,2,1,3,2,2,1,3,2,3,2,2,3,1,1,3,1,3,3,2,2,2,2,2,3,1,2,2,1,3,1,2,3,3,2,1,1,1,2,3,3,2,2,3,2,2,3,2,3,3,2,1,2,2,3,1,3,1,3,3,3,2,2,1,2,3,2,1,2,1,2,3,1,3,2,3,3,3,3,1,2,2,1,2,1,3,1,1,2,1,1,2,2,1,3,2,3,2,2,2,1,3,1,2,2,1,1,1,2,1,3,2,1,1,2,1,3,2,3,2,3,3,1,1,3,2,1,3,3,2,2,1,3,3,2,3,2,3,3,3,3,2,3,2,1,1,3,3,1,3,3,3,1,2,1,2,2,2,3,2,3,1,2,1,3,3,3,3,2,1,2,3,1,3,2,1,2,2,1,3,3,3,3,3,1,3,2,3,1,2,1,3,2,1,1,3,3,3,3,2,3,3,1,1,2,3,2,1,3,3,3,3,2,2,1,1,3,2,1,1,3,2,1,3,3,1,2,2,1,2,3,2,1,1,3,3,1,2,3,2,2,3,1,2,2,3,3,2,2,1,2,2,2,1,2,1,3,2,2,2,1,2,2,2,1,3,3,3,2,3,1,2,1,2,3,3,2,1,2,2,1,1,3,3,3,3,2,3,1,1,3,1,1,1,2,1,2,2,2,3,3,3,1,1,3,1,2,3,2,3,1,3,3,1,1,2,2,3,1,2,1,2,1,2,3,1,3,1,3,1,2,3,2,3,2,2,1,2,1,2,2,2,2,1,1,1,1,3,3,3,1,1,1,2,2,2,1,2,1,3,2,3,1,2,3,1,3,3,3,2,3,3,2,1,2,1,2,1,1,3,1,1,1,3,2,1,2,2,2,2,1,1,1,1,2,1,3,2,2,1,3,3,3,3,3,3,2,1,3,2,1,3,2,3,2,3,1,3,3,1,3,3,1,1,2,3,3,1,3,3,3,1,2,1,3,3,3,2,2,2,2,1,1,1,2,1,1,1,2,1,1,2,2,1,1,3,1,3,1,2,1,1,2,3,2,2,3,3,1,1,2,2,1,3,3,3,1,2,3,1,1,2,3,3,3,3,1,1,3,2,2,3,1,1,1,3,1,3,3,3,3,2,3,3,3,2,2,3,2,2,1,3,3,3,3,1,1,2,3,3,2,2,2,3,1,3,2,2,2,3,2,1,1,2,3,3,2,3,2,3,2,3,2,1,1,3,3,1,2,1,3,3,2,1,2,3,2,1,1,1,1,3,3,1,1,2,3,2,2,1,1,1,2,3,2,2,2,2,1,1,2,1,3,1,3,1,1,1,2,2,3,1,2,2,3,3,3,1,1,3,3,1,1,2,1,2,1,3,2,2,3,3,3,2,1,3,3,3,3,1,2,1,3,1,2,1,3,1,1,1,1,3,2,1,1,3,2,1,1,3,1,2,1,1,3,3,2,1,1,3,2,2,1,2,3,2,1,3,3,2,3,3,2,1,1,1,2,1,3,2,3,1,1,1,1,1,3,2,2,2,3,2,2,3,3,1,1,2,2,1,1,3,3,1,2,2,3,3,3,3,3,1,2,1,2,3,2,3,2,3,3,3,3,1,3,3,1,3,1,1,1,1,3,2,3,3,3,1,2,2,1,1,3,3,2,1,3,1,1,1,2,2,3,3,2,2,3,3,3,3,2,2,1,1,3,3,1,2,1,3,2,1,3,2,2,1,2,2,2,1,3,2,1,3,2,2,1,1,1,2,1,2,1,1,2,3,1,1,3,1,2,3,3,1,1,2,1,2,2,2,2,3,3,3,1,2,1,2,1,3,1,2,1,3,2,1,1,1,1,1,1,2,3,1,2,2,2,2,1,1,3,1,2,3,3,3,1,1,2,3,3,3,3,3,2,1,3,3,1,3,2,3,1,2,2,1,2,2,2,3,3,3,3,2,2,2,3,2,3,2,2,2,3,3,1,2,3,2,3,1,2,2,1,3,1,2,3,3,1,2,3,2,2,2,3,3,1,3,3,2,3,2,3,2,2,2,3,3,1,1,1,3,1,1,1,1,1,2,2,1,2,1,3,3,1,1,3,3,1,3,3,1,2,3,1,2,1,1,2,2,3,3,1,2,2,3,3,1,3,1,1,1,3,2,2,1,3,1,3,1,1,2,3,1,1,3,2,1,3,2,3,1,3,1,2,1,3,3,3,2,1,3,3,1,3,3,1,1,2,3,1,1,3,2,3,2,3,2,2,2,1,1,2,3,2,1,3,3,1,2,2,2,1,3,1,2,2,2,2,1,1,2,1,3,2,1,1,3,1,3,3,1,2,2,2,1,2,1,1,1,2,3,2,3,2,2,3,3,1,2,2,3,2,2,1,1,3,1,1,1,3,2,3,2,1,3,2,3,3,3,2,1,2,3,1,1,1,3,2,3,2,1,3,3,3,2,2,1,2,2,1,3,1,2,3,1,3,1,2,2,1,2,2,3,3,2,1,2,2,1,1,3,2,2,3,1,3,3,1,1,3,2,2,3,2,1,2,1,1,3,3,3,3,2,2,1,1,3,3,3,2,3,2,1,1,1,1,2,2,2,3,2,3,2,2,2,1,1,2,2,3,1,2,1,2,2,1,1,3,2,2,1,2,3,3,3,3,2,2,2,3,1,2,1,3,2,3,2,2,2,1,3,1,3,2,2,3,2,2,2,1,1,3,1,1,1,1,1,2,2,1,2,3,2,3,2,3,3,2,1,3,2,3,3,3,2,2,2,2,1,2,1,1,1,3,1,3,3,1,3,2,2,2,2,3,2,1,2,2,2,1,1,1,1,2,2,2,1,3,1,3,2,1,1,1,2,1,2,2,2,2,3,1,3,1,2,2,3,3,2,3,2,2,2,2,3,3,1,1,2,3,3,2,3,2,1,3,2,2,1,1,3,3,1,3,2,2,1,3,3,1,1,3,2,3,2,3,3,2,2,3,1,3,2,2,2,1,1,3,3,1,3,3,3,1,2,2,2,2,2,3,3,1,2,2,1,2,2,1,2,2,2,2,3,3,2,3,2,1,3,1,3,3,3,1,1,2,1,1,1,1,3,3,2,2,2,1,1,2,2,2,3,1,1,2,2,1,2,3,1,3,2,3,1,1,2,3,1,2,3,1,3,1,3,2,2,1,2,3,1,2,1,3,1,3,2,3,2,2,3,3,3,2,2,2,2,2,1,3,3,3,1,2,2,3,3,1,2,2,2,2,3,3,3,2,3,3,2,3,3,3,3,2,3,1,1,1,3,1,2,1,2,2,2,1,1,1,1,1,1,2,2,3,1,1,1,3,3,1,3,2,2,1,2,2,2,1,2,3,1,1,1,1,3,1,2,2,3,3,2,2,1,2,1,1,2,1,1,1,2,2,1,3,2,1,1,2,3,3,1,3,3,3,1,1,2,1,1,3,2,1,1,2,2,1,3,3,1,3,2,1,1,1,1,3,2,1,3,1,2,2,1,1,2,1,1,2,3,1,1,3,1,3,2,1,3,2,2,2,1,1,3,1,3,3,3,2,3,2,3,2,1,3,1,3,1,1,3,2,3,2,3,3,1,2,3,1,2,1,3,1,1,2,3,2,1,3,2,2,3,2,2,2,2,2,1,3,3,2,1,1,1,1,1,1,1,1,1,3,1,1,1,3,3,1,1,3,2,2,3,2,2,2,3,2,3,2,1,2,1,2,2,1,2,1,2,3,1,1,2,3,2,1,2,1,2,3,3,1,3,1,2,1,2,1,2,2,1,3,3,2,2,1,2,3,2,1,3,1,1,1,3,3,2,2,1,1,1,1,1,3,3,1,2,3,3,3,3,1,3,2,1,1,3,3,3,3,3,3,2,1,2,2,2,2,1,2,2,3,1,2,2,2,2,2,3,2,2,2,2,1,3,2,1,3,2,1,1,1,1,1,1,1,2,2,2,3,1,1,3,3,2,3,3,2,2,1,2,1,2,2,3,3,1,2,1,2,2,3,1,2,1,2,1,3,1,2,2,3,3,3,3,2,3,3,1,1,2,2,3,2,3,1,2,2,2,1,3,2,1,1,2,1,3,1,1,3,3,3,2,2,2,1,1,2,1,3,3,2,3,2,3,1,1,1,2,2,1,1,3,3,2,3,1,3,1,3,2,1,2,1,3,3,3,1,1,1,3,3,1,3,1,3,3,3,2,3,3,1,3,1,1,1,2,1,2,1,1,2,2,3,3,3,1,1,1,2,2,2,1,1,3,2,1,2,2,1,2,1,1,2,1,2,1,3,2,3,1,1,3,3,1,1,2,1,3,3,3,3,2,3,2,2,1,2,2,3,1,3,2,3,2,2,3,2,2,3,2,1,3,1,1,2,3,2,1,1,1,3,3,1,1,3,3,2,3,1,3,2,2,1,1,1,2,3,1,2,3,1,2,1,1,2,3,1,2,1,2,3,2,1,3,2,2,2,2,1,2,3,2,1,3,1,1,3,3,1,3,1,2,3,2,2,3,2,1,2,2,2,1,3,2,1,1,3,2,3,2,2,2,3,3,3,2,3,3,1,1,3,1,2,1,3,2,1,2,2,2,2,2,2,2,1,2,1,2,2,3,3,2,3,1,2,1,3,1,1,3,3,2,2,1,2,1,3,3,2,2,2,3,3,3,3,2,2,2,3,1,3,1,3,3,1,2,1,3,3,2,1,2,3,2,3,3,1,3,1,2,3,3,3,2,1,3,1,1,2,3,1,2,1,3,2,3,2,2,3,3,3,1,2,2,3,3,3,1,3,3,1,1,1,2,3,2,2,3,3,2,1,3,3,1,1,1,3,3,3,2,3,1,1,3,1,1,3,3,3,2,1,2,1,1,1,1,2,2,2,2,1,1,2,2,2,2,1,2,3,2,3,2,1,2,3,2,1,2,2,1,1,1,2,1,1,1,2,3,1,3,2,3,3,3,1,3,1,1,3,3,3,3,1,2,2,1,3,3,1,1,2,1,2,1,3,1,3,2,2,3,2,2,2,2,1,2,2,3,1,3,2,1,3,3,1,3,2,3,2,2,3,3,3,2,1,2,1,3,1,2,3,1,3,2,2,3,1,3,2,3,2,1,3,2,1,1,1,2,2,2,3,3,2,1,1,3,2,1,2,2,3,2,1,3,1,2,2,2,2,3,1,3,1,3,2,2,1,3,1,2,3,1,3,3,1,3,1,1,2,2,1,3,2,3,1,3,1,2,1,3,3,2,1,1,3,3,2,1,3,3,3,1,2,1,3,2,2,2,3,3,2,2,2,2,2,1,3,3,1,1,3,3,2,2,3,1,2,1,3,1,2,2,3,2,2,1,1,3,1,3,3,2,2,2,2,2,3,2,1,3,1,3,2,1,3,3,3,3,2,1,1,2,2,2,2,1,2,3,3,1,3,2,2,3,3,3,2,2,1,2,3,1,2,1,2,2,1,2,2,2,3,3,3,3,1,2,1,3,3,1,2,1,3,2,3,1,1,1,1,3,1,3,2,1,3,2,1,1,3,1,3,2,2,2,3,2,1,2,1,1,3,1,2,1,2,3,3,3,2,2,2,3,2,2,1,2,2,1,3,3,3,3,1,2,3,3,2,1,2,3,3,3,1,3,2,1,1,3,2,3,2,1,1,1,2,1,1,1,1,2,2,2,2,2,3,2,1,3,2,1,2,1,1,3,2,3,1,1,2,1,3,3,3,2,3,1,2,1,1,1,2,2,1,3,2,3,2,2,1,3,3,2,3,2,1,3,2,1,3,2,1,2,3,1,3,2,2,2,3,1,3,1,2,1,1,1,1,1,2,3,3,2,1,2,2,3,3,3,3,2,1,1,3,2,2,3,2,3,2,1,1,1,3,1,3,3,1,1,2,1,3,3,2,2,1,2,1,2,1,3,2,3,3,1,1,2,2,3,2,2,3,1,3,3,2,3,1,3,1,2,1,2,3,3,2,2,3,2,2,2,3,2,2,1,3,2,3,3,1,1,1,1,2,2,3,1,3,2,1,2,2,3,1,3,3,1,3,3,2,1,2,1,2,3,1,1,2,3,2,3,2,2,2,3,2,3,3,2,1,3,1,1,1,1,3,2,3,2,2,1,3,1,2,2,2,1,2,1,1,3,3,3,3,1,2,3,2,3,3,2,1,1,3,2,1,1,3,2,3,1,1,3,1,3,3,3,1,1,2,1,2,3,3,3,3,1,1,1,1,1,2,3,2,1,2,3,1,1,1,1,1,2,2,3,1,3,3,3,1,1,3,2,1,2,2,2,3,3,3,1,3,2,2,1,3,2,1,3,1,1,1,3,2,2,3,1,1,3,1,2,2,2,3,3,1,1,2,1,3,2,1,2,3,3,2,1,3,2,2,3,3,1,3,2,2,3,1,2,1,1,1,1,1,2,1,3,3,1,1,1,1,2,1,3,3,2,1,1,2,2,2,3,1,2,2,3,1,3,3,3,1,2,1,2,3,1,3,3,3,3,3,1,3,3,3,2,1,3,2,1,1,1,3,2,3,2,2,1,1,2,1,1,2,2,1,1,2,1,3,2,3,3,2,1,3,2,1,3,3,2,2,3,3,2,1,3,2,1,1,2,2,1,3,2,2,3,1,1,3,3,1,1,3,2,2,3,2,1,1,1,3,3,1,3,1,3,1,2,2,1,2,3,3,3,1,2,1,2,1,3,3,3,2,3,2,1,1,1,1,3,1,1,2,2,3,1,2,3,1,2,3,3,2,1,3,1,2,3,3,3,1,2,3,3,2,1,1,3,3,3,3,3,3,3,3,1,1,3,1,3,1,2,3,1,2,2,1,1,1,1,3,3,2,2,3,2,3,3,1,3,3,3,3,2,3,1,1,1,1,1,2,1,2,2,2,3,2,1,2,1,2,1,1,1,1,3,1,3,2,1,1,3,1,1,3,2,2,3,2,1,2,3,1,2,3,3,2,2,1,3,1,2,2,1,3,1,1,2,1,3,3,3,3,3,2,2,1,1,3,3,1,3,3,3,1,3,1,3,1,2,3,2,2,2,3,3,2,2,3,3,3,1,2,2,1,3,1,3,2,1,2,3,1,3,3,2,2,2,3,1,2,1,1,2,2,1,2,3,1,1,2,1,3,1,1,1,1,1,2,2,2,3,1,1,1,2,3,3,3,2,1,2,1,3,2,3,2,2,1,3,1,1,1,2,3,3,3,1,1,3,3,1,3,3,2,3,2,3,1,1,3,3,2,1,1,2,1,1,2,2,1,3,2,1,2,1,2,2,2,2,1,3,1,1,3,3,3,3,3,3,2,3,2,1,1,3,2,1,1,1,2,1,2,2,1,3,1,2,2,1,2,3,3,2,1,2,1,1,3,3,3,3,3,2,2,2,2,1,1,1,2,2,2,3,2,1,2,1,2,3,2,3,1,1,3,3,2,1,2,2,1,2,3,1,2,1,2,3,2,2,1,2,3,3,3,2,1,1,2,1,3,3,1,2,2,2,3,2,2,2,3,2,3,2,2,2,3,1,2,1,3,1,2,3,3,2,3,1,3,2,2,1,1,2,1,3,2,2,3,2,2,2,1,1,3,3,2,1,1,2,3,3,1,1,1,3,3,3,2,1,2,1,1,2,3,1,2,3,1,3,1,2,2,2,2,2,3,2,3,1,2,1,3,3,3,1,3,2,1,2,3,3,2,1,1,2,2,1,1,1,3,3,3,2,1,3,1,3,3,1,2,3,3,2,3,2,3,2,1,3,3,3,3,1,2,3,3,1,2,2,1,1,1,3,2,2,2,2,2,1,3,2,3,1,3,2,2,3,1,1,3,2,3,3,2,1,3,2,2,2,1,3,2,2,1,1,2,2,1,3,3,3,1,2,2,3,2,3,1,2,3,2,3,1,2,3,3,3,2,1,2,3,1,2,1,2,1,2,3,1,1,2,1,3,3,3,2,1,3,2,3,2,1,2,2,3,3,2,3,1,3,3,2,2,1,2,3,3,3,3,1,2,3,3,2,2,2,2,2,3,3,3,2,3,2,1,3,2,3,2,3,2,3,1,1,3,2,3,2,1,2,3,3,2,1,3,3,1,3,3,1,1,2,1,3,3,3,1,3,3,1,2,1,1,3,2,1,3,3,1,3,1,1,1,1,2,1,3,2,2,3,1,1,1,2,3,2,3,2,2,2,1,3,3,3,2,3,3,2,1,3,3,3,3,2,3,3,1,3,3,1,3,2,1,2,2,1,2,2,2,3,2,2,1,3,2,2,1,3,1,3,1,1,2,2,2,2,2,3,2,2,2,2,3,2,2,3,2,1,3,3,2,1,1,1,1,3,2,3,2,1,2,2,1,1,2,2,1,3,3,2,3,3,3,1,2,2,2,1,2,2,2,2,2,3,1,2,3,3,2,2,1,1,2,3,2,3,1,1,1,2,2,2,3,1,2,2,2,2,1,2,2,3,1,2,3,2,2,2,1,1,1,3,3,1,3,1,3,3,2,2,3,2,2,3,1,1,1,2,2,1,2,3,1,3,1,3,2,2,1,1,1,2,1,3,3,3,3,3,1,1,3,2,2,2,3,3,1,2,3,3,2,3,1,3,3,1,3,2,2,3,2,3,1,3,1,3,3,2,2,2,3,3,2,3,3,1,2,2,2,3,2,1,3,2,1,1,2,3,3,1,3,3,3,2,3,1,3,3,3,1,1,1,1,1,1,3,2,2,2,1,3,2,2,3,1,3,1,1,2,3,3,2,1,1,3,3,3,3,3,2,1,3,1,3,1,3,2,3,1,2,1,3,2,1,2,2,2,1,1,3,1,2,1,1,2,1,1,1,3,1,1,1,2,3,2,1,2,2,3,1,1,3,3,2,3,2,1,2,3,1,3,2,3,1,2,1,1,1,2,1,2,2,1,1,1,1,1,1,3,1,1,1,3,3,2,2,1,3,2,1,2,3,3,3,0,0,0]
    # nums = [2,2,0,2,0,2,0,0,2,0]
    print(s.canJump(nums))