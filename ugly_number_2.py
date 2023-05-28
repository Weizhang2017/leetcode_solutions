# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        a = b = c = 0
        while len(l) < n:
            if min(2*l[a], 3*l[b], 5*l[c]) > l[-1]:
                l.append(min(2*l[a], 3*l[b], 5*l[c]))
            if l[-1] == 2*l[a]:
                a += 1
            elif l[-1] == 3*l[b]:
                b += 1
            else:
                c += 1
        return l[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(1))