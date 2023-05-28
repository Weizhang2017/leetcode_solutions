from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = False
        # print(nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] > nums[i]:
                found = True
                break
        if not found:
            return sorted(nums)
        else:
            for j in range(len(nums)-1, -1, -1):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = sorted(nums[i+1:])
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([3,2,1]))