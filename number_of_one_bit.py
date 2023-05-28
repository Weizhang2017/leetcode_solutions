class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            counter += n % 2
            n //= 2
        return counter

if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(3))