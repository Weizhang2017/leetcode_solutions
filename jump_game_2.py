# https://leetcode.com/problems/jump-game-ii
from typing import List

class Solution:
    counter = 0
    ind = 0
    steps = []
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(1, nums[0]+1):
            # print(self.counter, '+', nums) 
            if i < len(nums) - 1:
                self.counter += 1
                # print(self.counter, '+1')
                self.jump(nums[i:])
                self.counter -= 1
                # print(self.counter, '-') 
            elif i == len(nums) - 1:
                self.counter += 1
                # print(self.counter, '+2')
                self.steps.append(self.counter)
                self.counter -= 1
        return min(self.steps)


if __name__ == '__main__':
    s = Solution()
    print(s.jump([1,2,3]))
