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


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         LIS = [1] * len(nums)

#         for i in range(len(nums)-1, -1, -1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] < nums[j]:
#                     LIS[i] = max(LIS[i], 1 + LIS[j])
        
#         return max(LIS)

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for x in nums:
            # Find the insertion index of x in tails
            idx = bisect_left(tails, x)

            # if x  is larger than all elements, append it
            if idx == len(tails):
                tails.append(x)
            else:
                # Replace the existing element with a smaller tail
                tails[idx] = x
        return len(tails)