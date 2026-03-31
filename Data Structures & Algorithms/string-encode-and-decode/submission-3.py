class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            # extract the length and convert it
            length = int(s[i:j])

            # read the length of the string, and 
            # get the start of the string

            start = j + 1
            end = start + length

            res.append(s[start:end])


            # move the pointer to the start of the next encoded block
            i = end

        return res

