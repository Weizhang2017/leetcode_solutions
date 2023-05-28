# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = [[] for _ in range(numRows)]
        n = 0
        f = self.plus
        counter = 0
        while n < len(s):
            print(counter)
            l[counter].append(s[n])
            if counter == 0:
                f = self.plus
            elif counter == numRows - 1:
                f = self.minus
            counter = f(counter)
            n += 1
        s_ = ''
        for r in range(numRows):
            s_ += ''.join(l[r])
        return s_

    def plus(self, counter):
        return counter + 1

    def minus(self, counter):
        return counter - 1


if __name__ == '__main__':
    s = Solution()
    print(s.convert('AB', 1))