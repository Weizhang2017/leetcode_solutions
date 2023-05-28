# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    index = 0
    init = None
    def search(self, nums: List[int], target: int) -> int:
        if self.init is None:
            self.init = nums[0]
        if not nums or (len(nums) == 1 and nums[0] != target):
            return -1
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid + self.index
        elif self.init == target:
            return self.index
        elif target > self.init > nums[mid]:
            return self.search(nums[:mid], target)
        elif nums[mid] < target < self.init:
            self.index += mid + 1
            return self.search(nums[mid+1:], target)
        elif target < nums[mid] < self.init or self.init < target < nums[mid]:
            return self.search(nums[:mid], target)
        elif target < self.init < nums[mid] or target > nums[mid] > self.init:
            self.index += mid + 1
            return self.search(nums[mid+1:], target)

if __name__ == '__main__':
    s = Solution()
    print(s.search([0,1,3,6,8], 2))
