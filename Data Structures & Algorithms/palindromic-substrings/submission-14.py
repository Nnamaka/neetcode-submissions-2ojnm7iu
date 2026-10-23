# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         total_palindromes = 0

#         def count_around_center(left: int, right: int) -> int:
#             count = 0

#             # Expand outwards as long as the substing remains a valid palindrome
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 count += 1
#                 left -= 1
#                 right += 1
#             return count

#         for i in range(len(s)):
#             # odd-length palindromes (center at i)
#             total_palindromes += count_around_center(i,i)

#             # Even-length palindromes (center between i and i + 1)
#             total_palindromes += count_around_center(i, i + 1)

#         return total_palindromes

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_p = 0

        #initialize the dp matrix
        dp = [[False] * n for _ in range(n)]

        #initialize the diagonal
        for i in range(n):
            dp[i][i] = True

        # bottom-up dp aproach
        for i in range(n-1, -1, -1):
           
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i<=2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        total_p += 1
        
        return total_p 
        
