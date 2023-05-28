# https://leetcode.com/problems/summary-ranges/
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums:
            interval = [[nums[0], nums[0]]]
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] > 1:
                    interval[-1][1] = nums[i-1]
                    interval.append([nums[i], nums[i]])
            interval[-1][1] = nums[-1]
            return [f'{item[0]}->{item[1]}' if item[0] != item[1] else f'{item[0]}' for item in interval  ]
        else:
            return []

if __name__ == '__main__':
    s = Solution()
    print(s.summaryRanges([0,2,3,4,6,8,9]))