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