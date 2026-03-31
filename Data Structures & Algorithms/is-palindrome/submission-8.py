class Solution:
    def isPalindrome(self, s: str) -> bool:

        # loop through the string with pointers
        f_p = 0
        s_p = len(s) - 1

        while f_p < s_p:
            # 1. Skip non-alphanumeric characters from the front
            while f_p < s_p and not s[f_p].isalnum():
                f_p += 1
            
            # 2. Skip non-alphanumeric characters from the back
            while f_p < s_p and not s[s_p].isalnum():
                s_p -= 1
            
            # 3. Compare the characters (case-insensitive)
            if s[f_p].lower() != s[s_p].lower():
                return False
            
            f_p += 1
            s_p -= 1

        return True