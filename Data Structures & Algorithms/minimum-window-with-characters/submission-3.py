from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""
        
        # store t characters and the dynamic window gotten from 
        # s, in a dictionary/hashmap for O(1) lookup
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # create variable to monitor existence of characters in current
        # window

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # check very well. it is at this point that we keep track of
            # the number of valid 't' characters that appear in our window.
            # the logic here also makes sure that if a valid character 
            # appears twice in our window, the duplicate is not counted;
            # the code "window[c] == countT[c]" takes care of that
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""




#SECOND SOLUTION
def minWindow(s, t):
    if not t or not s:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)

    # Left and Right pointer
    l, r = 0, 0


    # formed is used to keep track of how many unique characters in t are
    # present in the current window in its desired frequency.

    formed = 0
    window_counts = {}


    # (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        # try and contract the window till the point where it ceases to be
        # valid
        while l <= r and formed == required:
            char = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
                
