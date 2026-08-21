class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buy= prices[0]
    
        # profit = sell - buy

        for i in range(0,len(prices)):
            profit = prices[i] - lowest_buy
            max_profit = max(max_profit, profit)
            lowest_buy = min(lowest_buy, prices[i])


        return max_profit



        