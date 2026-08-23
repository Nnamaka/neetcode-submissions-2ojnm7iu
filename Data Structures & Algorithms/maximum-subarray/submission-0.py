class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            # if curr_sum was negative, reset it
            curr_sum = max(n, curr_sum + n)
            max_sum = max(max_sum, curr_sum)

        return max_sum
        