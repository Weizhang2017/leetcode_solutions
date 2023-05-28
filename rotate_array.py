from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        i = k % n
        if i == 0:
            return nums
        nums[:i], nums[i:] = nums[-i:], nums[:-i]
        
        return nums
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7,9]
    k = 3
    print(s.rotate(nums, k))