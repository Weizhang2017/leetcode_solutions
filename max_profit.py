class Solution:
    def maxProfit(self, prices: list) -> int:
        profit_ = profit = 0
        for i in range(len(prices)-1):
            profit_ += prices[i+1] - prices[i]
            profit_ = max(0, profit_)
            profit = max(profit, profit_)
        return max(0, profit)

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))