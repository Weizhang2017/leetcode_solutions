class Solution:
    def missingNumber(self, nums) -> int:
        l = [0] * (len(nums)+1)
        for i in nums:
            l[i] = 1
        
        for i in range(len(l)):
            if l[i] == 0:
                return i

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3,0,1]))