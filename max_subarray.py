from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = []
        n = len(nums)
        if n == 1: return nums[0]
        elif n == 2: return max(nums[0], nums[1], nums[0]+nums[1])
        a = nums[0] + nums[1]
        b = max(nums[1], a)
        max_ = max(a,b,nums[0])
        for i in range(2, n):
            a = max(a, b) + nums[i]
            b = max(nums[i], a)
            if max(a, b) > max_:
                max_ = max(a, b)

        return max_

if __name__ == '__main__':
    s = Solution()
    nums = [1,-1,-2]
    print(s.maxSubArray(nums))