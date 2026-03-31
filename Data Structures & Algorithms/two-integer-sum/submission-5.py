class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}
        indices = []
        for i, n in enumerate(nums):
            diff = target - n

            if diff in array:
                indices += sorted([array[diff] , i])
                return indices

            array[n] = i
        
        return indices