# Bottom-up approach 2D DP
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # initialize a single row with 1s
#         row = [1] * n

#         for i in range(m - 1):
#             newRow = [1] * n

#             for j in range(n - 2, -1, -1):
#                 newRow[j] = newRow[j + 1] + row[j]
#             row = newRow
#         return row[0]

# import math

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return math.comb(m + n - 2, m - 1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_row = [1] * n

        # db = [ [1] * n for _ in range(m) ]

        for i in range(m - 2, -1, -1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + dp_row[j]

            dp_row = new_row
        return dp_row[0]

  