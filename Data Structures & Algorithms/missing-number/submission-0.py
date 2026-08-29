class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = n # initialize with n so the complete range [0, n] is covered

        for i, num in enumerate(nums):
            # XOR index i and value num into missing
            missing ^= i ^ num

        return missing