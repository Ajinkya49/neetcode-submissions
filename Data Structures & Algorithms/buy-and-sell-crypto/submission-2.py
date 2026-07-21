class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        min_profit = float('infinity')
        n = len(prices)

        for i in range(0,n):
            min_profit = min(min_profit,prices[i])
            maxprofit = max(maxprofit,prices[i]-min_profit)
            
        return maxprofit


