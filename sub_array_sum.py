# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    	coutner = 0
    	s_i = nums[0]
    	if s_i == k: coutner += 1
    	for i in range(1, len(nums)):
    		s_i += nums[i]
    		if s_i == k: coutner += 1
    		s_j = nums[0]
    		s_i_j = s_i - s_j
    		if s_i_j == k: coutner += 1
    		for j in range(1, i):
    			s_j += nums[j] 
    			s_i_j = s_i - s_j
    			if s_i_j == k: coutner += 1
    	return coutner

    def subarraySum2(self, nums: List[int], k: int) -> int:
    	coutner = 0
    	d = {0: 1}
    	s = 0
    	for i in range(len(nums)):
    		s += nums[i]
    		if s - k in d:
    			coutner += d[s-k]
    		d[s] = d.get(s, 0) + 1
    	return coutner


if __name__ == '__main__':
	s = Solution()
	print(s.subarraySum2([1,2,3], 3))
