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
                
