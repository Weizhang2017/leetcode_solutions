from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            b, a = max(a + nums[i], b), b
        return max(a, b)

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,1,3,100]
    print(s.rob(nums))
