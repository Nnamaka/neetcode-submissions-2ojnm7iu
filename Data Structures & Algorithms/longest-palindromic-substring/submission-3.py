class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""

        res = ""
        res_len = 0


        def expand_around_center( left: int, right: int) -> str:
            # Ecapnad outwards while valid and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # return the palindrome slice found (left + 1 to right)
            return s[left + 1:right]

        for i in range(len(s)):
            # odd length palindromes (e.g. "aba", center at i)
            p1 = expand_around_center(i, i)
            if len(p1) > res_len:
                res = p1
                res_len = len(p1)
            
            # Even length palindromes (e.g "abba", center between i and i + 1)
            p2 = expand_around_center(i, i + 1)
            if len(p2) > res_len:
                res = p2
                res_len = len(p2)
        return res
        


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2:
#             return s

#         dp = [[False] * n for _ in range(n)]
#         start, max_len = 0, 1

#         # Base cases: single characters are palindromes
#         for i in range(n):
#             dp[i][i] = True

#         # Fill table bottom-up
#         for i in range(n - 1, -1, -1):
#             for j in range(i + 1, n):
#                 if s[i] == s[j]:
#                     if j - i <= 2 or dp[i + 1][j - 1]:
#                         dp[i][j] = True
#                         if (j - i + 1) > max_len:
#                             max_len = j - i + 1
#                             start = i

#         return s[start:start + max_len]