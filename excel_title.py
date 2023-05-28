class Solution:
    l = 'abcdefghijklmnopqrstuvwxyz'
    def convertToTitle(self, columnNumber: int) -> str:
        columnNumber_ = columnNumber // 26
        if columnNumber_ > 0 and columnNumber != 26:
            if columnNumber % 26:
                return self.convertToTitle(columnNumber_) + self.l[(columnNumber-1) % 26].upper()
            else:
                return self.convertToTitle(columnNumber_-1) + self.l[(columnNumber-1) % 26].upper()
        else:
            return self.l[(columnNumber-1) % 26].upper()

if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(701))
