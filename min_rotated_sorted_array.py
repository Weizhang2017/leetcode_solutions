from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
    	n = len(nums)
    	if n <= 3:
    		min_ = nums[0]
    		for i in nums[1:]:
    			if min_ > i:
    				min_ = i
    		return min_
    	else:
    		if nums[n//2] > nums[0] > nums[-1]:
    			return self.findMin(nums[n//2:])
    		else:
    			return self.findMin(nums[:n//2+1])
if __name__ == '__main__':
	nums = [11,13,15,17]
	s = Solution()
	print(s.findMin(nums))