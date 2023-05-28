# https://leetcode.com/problems/number-complement/
class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        num_ = num
        while num_:
            num_ //= 2
            count += 1
        sum_ = 2**count - 1
        return  sum_ -  num

if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))