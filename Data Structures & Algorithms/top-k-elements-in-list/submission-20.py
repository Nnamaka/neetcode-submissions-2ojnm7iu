# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elements = defaultdict()

        for n in nums:
            elements[n] = 1 + elements.get(n, 0)

        result = []

        bucket = [[] for _ in range(len(nums) + 1)]


        for key, value in elements.items():
            bucket[value].append(key)

        for i in range(len(bucket) - 1, -1, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result

        return result