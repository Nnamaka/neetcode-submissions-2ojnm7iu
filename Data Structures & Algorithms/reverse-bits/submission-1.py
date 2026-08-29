class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # make space in res, then pull the rightmost bit from n
            res = (res << 1) | (n & 1)
            # shift n right to process the next bit

            n >>= 1
        return res