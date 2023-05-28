class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        while n != 1:
            if n % 4:
                return False
            else:
                n //= 4
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(0))