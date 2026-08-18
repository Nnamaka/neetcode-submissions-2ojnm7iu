class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear( houses: List[int]) -> int:
            rob1, rob2 = 0, 0

            # max( rob2, n + rob1)
            for n in houses:
                highest_value = max(rob2, n + rob1)
                rob1 = rob2
                rob2 = highest_value

            return rob2

        return max( rob_linear(nums[:-1]), rob_linear(nums[1:]))


        