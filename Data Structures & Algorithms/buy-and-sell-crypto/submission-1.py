class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # define a variable to hold the max profit
        max_profit = 0
        # I can use a nested for loop to solve this
        for buy in range( len(prices)):
            for sell in range( buy, len(prices)):

                if prices[sell] - prices[buy] > max_profit:
                    max_profit = prices[sell] - prices[buy]
        
        return max_profit
