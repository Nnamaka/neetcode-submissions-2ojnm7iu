# try and solve this recursively like you were doing below

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         length = 0

#         def getLength( pos:int ):

#             if pos == len(nums) - 1:
#                 return
#             if nums[pos] - 1 == nums[pos - 1]:
#                 length += 1

#             return max(length, getLength(pos + 1))
        
#         return getLength(0)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            # check if 'n' is the start of a sequence

            if (n - 1) not in numset:
                length = 1

                # Build the sequence
                while (n + length ) in numset:
                    length += 1

                longest = max(length, longest)

        return longest

