from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            upper = len(nums) - 1
            lower = 0
            mid = (upper + lower) // 2
            while upper >= lower:
                if target < nums[mid]:
                    upper = mid - 1
                    mid = (upper + lower) // 2
                elif target > nums[mid]:
                    lower = mid + 1
                    mid = (upper + lower) // 2
                else:
                    down = up = mid
                    print(down, up, nums[down])
                    while down >= 0 and nums[down] == target:
                        if nums[down] == target:
                            down -= 1
                    while up <= len(nums) - 1 and nums[up] == target:
                        if nums[up] == target:
                            up += 1
                    return [down+1, up-1]
        return [-1, -1]

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([2,2],7))