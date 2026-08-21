# class Solution:


#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         # Base case: Each element is an LIS of length 1
#         dp = [1] * len(nums)

#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], 1 + dp[j])
        
#         return max(dp)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)