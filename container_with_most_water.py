# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        pointer1 = 0
        pointer2 = len(height) - 1
        while pointer1 < pointer2:
            max_area = max(max_area, (pointer2 - pointer1) * min(height[pointer1], height[pointer2]))
            if height[pointer1] < height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))