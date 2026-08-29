class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            # ans[i >> 1] gets set bits of i // 2
            # (i & 1) adds 1 if the rightmost bit of i is 1
            ans[i] = ans[i >> 1] + (i & 1)
        return ans