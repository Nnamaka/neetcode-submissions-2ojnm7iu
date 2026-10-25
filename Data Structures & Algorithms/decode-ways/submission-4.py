# class Solution:
#     def numDecodings(self, s: str) -> int:

#         if not s or s[0] == '0':
#             return 0 

#         # Base cases
#         # Equivalent to dp[0]
#         two_steps_back = 1

#         # Equivalent to dp[1] 
#         one_step_back = 1 

#         for i in range(1, len(s)):
#             current = 0

#             # 1-digit check (must be '1' - '9')
#             if s[i] != '0':
#                 current += one_step_back

#             # 2-digit check (must be '10'-'26')
#             two_digit = int(s[i - 1: i + 1])
#             if 10 <= two_digit <= 26:
#                 current += two_steps_back

#             # Early exit if an invalid configuration makes decoding impossible

#             if current == 0:
#                 return 0

#             # Advance sliding state variables
#             two_steps_back = one_step_back
#             one_step_back = current

#         return one_step_back


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if ( i + 1 < len(s) and ( s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)


















