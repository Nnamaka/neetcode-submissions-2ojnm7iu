class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one
        
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         sone, stwo = 1, 2

#         for n in range(2, n ):
#             ways = sone + stwo
#             sone = stwo
#             stwo = ways
#         return ways
        