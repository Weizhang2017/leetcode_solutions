# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        for key in d:
            for i in range(len(d[key])-1):
                if abs(d[key][i] - d[key][i+1]) <= k:
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,1,2,3]
    k = 3
    print(s.containsNearbyDuplicate(nums, k))