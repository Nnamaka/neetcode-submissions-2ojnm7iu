class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        length = 0
        l = 0

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while ((r-l)+1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1

            length = max(length, (r-l+1))
        return length