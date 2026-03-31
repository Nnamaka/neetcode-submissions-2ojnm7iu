class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # step 1 - sorting is crucial
        nums.sort()

        for i in range(len(nums)):

            # skip the same value to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # use two pointers for the rest of the array
            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # found a triplet!
                    res.append([nums[i], nums[l], nums[r]])

                    # update pointers and skip duplicates for 'l'
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

