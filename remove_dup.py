from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0
        for i in range(2, n):
            if nums[i-2-counter] == nums[i-counter]:
                nums[i-counter:-1] = nums[i+1-counter:]
                counter += 1
        return len(nums) - counter

if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    print(s.removeDuplicates(nums))