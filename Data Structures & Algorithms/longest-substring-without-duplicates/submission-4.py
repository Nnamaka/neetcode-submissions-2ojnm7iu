
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = set()
        length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l += 1
                
            string.add(s[r])
            length = max(length, (r-l) + 1)

                
        return length