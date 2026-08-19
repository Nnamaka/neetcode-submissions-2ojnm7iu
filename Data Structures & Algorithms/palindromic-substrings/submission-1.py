class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palindromes = 0

        def count_around_center(left: int, right: int) -> int:
            count = 0

            # Expand outwards as long as the substing remains a valid palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            # odd-length palindromes (center at i)
            total_palindromes += count_around_center(i,i)

            # Even-length palindromes (center between i and i + 1)
            total_palindromes += count_around_center(i, i + 1)

        return total_palindromes
        