# class Solution:

#     def encode(self, strs: List[str]) -> str:

#     def decode(self, s: str) -> List[str]:

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        
        return encoded_string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Step 1. Find the delimiter to determine where the length ends
            j = i

            while s[j] != '#':
                j += 1

            # step 2. Extract the length and convert to int
            length = int(s[i:j])

            # step 3. Read the exact number of characters specified by length
            # and append it to result

            # The string starts right after the '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])

            i = end
        return res
