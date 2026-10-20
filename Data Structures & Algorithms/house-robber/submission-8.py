class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n + 1]
        for n in nums:
            big_value = max(rob2, n + rob1)
            rob1 = rob2
            rob2 = big_value
        
        return rob2

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         max_robbed = nums[0]
#         houses = len(nums)
#         for n in range(houses):
#             if n + 2 < houses:
#                 nums[n+2] = nums[n+2] + nums[n]
#                 max_robbed = max(max_robbed, nums[n+2], nums[n])
#             max_robbed = max(max_robbed, nums[n])
            
#         return max_robbed
