class Solution:
    numbers = set()
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n in self.numbers:
            return False
        else:
            self.numbers.add(n)
            sum_ = 0
            while n:
                sum_ += (n % 10) ** 2
                n //= 10
            return self.isHappy(sum_)


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(10))