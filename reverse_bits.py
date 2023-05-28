class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0] * 32
        i = 0
        while n:
            bits[i] = n % 2
            n = n // 2
            i += 1
        number = 0

        for i in range(len(bits)):
            number += bits[i] * 2 ** (len(bits) - i - 1)
        return number

if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))