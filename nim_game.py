# https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        remainder = n % 6
        if 5 > remainder > 3:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    print(s.canWinNim(5))
