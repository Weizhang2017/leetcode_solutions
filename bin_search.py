from typing import List

class Solution:
    ind = 0
    def search(self, nums: List[int], target: int) -> int:
        if nums:
            l = len(nums)
            if nums[l//2] == target:
                return self.ind + l//2
            elif nums[l//2] < target:
                self.ind += l//2 + 1
                return self.search(nums[l//2+1:], target)
            else:
                return self.search(nums[:l//2], target)
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1,9]
    target = 9
    print(s.search(nums, target))