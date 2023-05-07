# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [7,1,5,3,6,4]

        max_profit = 0
        buy = 0
        sell = buy + 1

        for i in range(len(prices)-1):
            profit = prices[sell] - prices[buy]

            if prices[buy] > prices[sell]:
                buy = sell
                sell = buy + 1
            
            else:
                if profit > max_profit:
                    max_profit = profit

                sell += 1

        return max_profit