# DP Top-down approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)
        # Initialize (m+1) x (n+1) grid filled with 0s
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m, n = len(text1), len(text2)
#         # Initialize (m+1) x (n+1) grid filled with 0s
#         dp = [[0] * (n + 1) for _ in range(m + 1)]

#         for i in range(m-1,-1,- 1):
#             for j in range( n-1, -1, -1):
#                 if text1[i] == text2[j]:
#                     dp[i][j] = 1 + dp[i + 1][j + 1]
#                 else:
#                     dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
#         return dp[0][0]