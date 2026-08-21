class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # Handle 1-element arrays and negative defaults
        curr_min, curr_max = 1, 1


        for n in nums:
            # Multiplicative identity reset when encountering 0
            if n == 0:
                curr_min, curr_max = 1, 1
                continue

            # Store temporary value before updating curr_max
            tmp = curr_max * n
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(tmp, n * curr_min, n)

            res = max(res, curr_max)

        return res