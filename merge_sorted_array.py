#https://leetcode.com/problems/merge-sorted-array/
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not len(nums1):
            nums1 = nums2[:n]
        elif not len(nums2):
            nums1 = nums1[:m]
        else:
            i = j = 0
            while i < m or j < n:
                if j < n and i < m and nums1[i] <= nums2[j]:
                    i += 1
                elif j >= n:
                    i += 1
                else:
                    nums1.insert(i, nums2[j])
                    i += 1
                    m += 1
                    j += 1
            for _ in range(len(nums1) - m):
                nums1.pop()
        # if i < m:
        #     nums1 = nums1[:j+m]
        # if j < n:
        #     nums1 += nums2
        
if __name__ == '__main__':
    s = Solution()
    s.merge([2,0],1,[1],1)