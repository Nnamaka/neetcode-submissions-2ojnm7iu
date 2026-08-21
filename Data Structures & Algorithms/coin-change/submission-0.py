class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize DP table with an upper bound (amount + 1)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # Base case: 0 amount needs 0 coins

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        # if dp[amount] was not updated, it's impossible to form the amount
        return dp[amount] if dp[amount] != amount + 1 else -1