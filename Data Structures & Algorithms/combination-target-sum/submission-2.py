class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start: int, current: List[int], remaining: int):
            if remaining == 0:
                result.append(list(current))
                return

            for i in range(start, len(nums)):
                if remaining - nums[i] < 0:
                    break
                
                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])
                current.pop()

        backtrack(0, [], target)
        return result


# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []

#         def backtrack(i: int, current_combo: List[int], current_sum: int):
#             # Base Case 1: Target reached
#             if current_sum == target:
#                 res.append(current_combo.copy())
#                 return
            
#             # Base Case 2: Exceeded target or out of bounds
#             if current_sum > target or i >= len(nums):
#                 return

#             # Decision 1: Include nums[i] (can reuse, so index remains i)
#             current_combo.append(nums[i])
#             backtrack(i, current_combo, current_sum + nums[i])
            
#             # Backtrack (undo decision)
#             current_combo.pop()

#             # Decision 2: Skip nums[i] and move to next index i + 1
#             backtrack(i + 1, current_combo, current_sum)

#         backtrack(0, [], 0)
#         return res