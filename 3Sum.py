# https://leetcode.com/problems/3sum/
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i], nums[j], nums[k]] not in l:
                        l.append([nums[i], nums[j], nums[k]])
                    j -= 1
                    i += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                else:
                    i += 1
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-2,0,1,1,2]))