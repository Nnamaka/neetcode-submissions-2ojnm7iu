# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         word_set = set(wordDict)
#         dp = [False] * (len(s) + 1)
#         dp[0] = True # Base case: empty string

#         for i in range(1, len(s) + 1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in word_set:
#                     dp[i] = True
#                     break

#         return dp[len(s)]

from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        # Queue stores valid starting indices to search from
        queue = deque([0])

        # 'visited' stores indices we've already evaluated to prevent duplicate work
        visited = set()

        while queue:
            start = queue.popleft()

            if start in visited:
                continue
            visited.add(start)


            # Try matching words of various starting from 'start'
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    # if we reached the end of the string, we successfully broke the word!
                    if end == len(s):
                        return True

                    # otherwise, 'end'becomes a valid starting index for the next word
                    queue.append(end)

        return False