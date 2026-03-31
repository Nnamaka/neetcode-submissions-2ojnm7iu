class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)- 1
        small = float("inf")

        while l <= r:

            if nums[l] > nums[r]:
                small = nums[r]
            elif nums[l] < small:
                small = nums[l]
            else:
                pass
            l += 1
            r -= 1

        return small if small != float("inf") else nums[0]