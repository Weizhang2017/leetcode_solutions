# https://leetcode.com/problems/4sum/
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    	if len(nums) < 4:
    		return []
    	nums.sort()
    	n = len(nums)
    	l = []
    	for i in range(n):
    		for j in range(i+1, n):
    			a = j + 1
    			b = n - 1
    			while a < b:
    				if nums[i] + nums[j] + nums[a] + nums[b] < target:
    					a += 1
    				elif nums[i] + nums[j] + nums[a] + nums[b] > target:
    					b -= 1
    				else:
    					if [nums[i], nums[j], nums[a], nums[b]] not in l:
	    					l.append([nums[i], nums[j], nums[a], nums[b]])
    					a += 1
    					b -= 1
    	
    	return l

if __name__ == '__main__':
	s = Solution()
	print(s.fourSum([2,2,2,2,2], 8))