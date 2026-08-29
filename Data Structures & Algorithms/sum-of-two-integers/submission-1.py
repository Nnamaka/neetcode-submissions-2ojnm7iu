class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            # carry bitwise calculation
            carry = (a & b) << 1

            # Add without carry, restricted to 32 bits
            a = (a ^ b) & MASK

            # update b with carry, restricted to 32bits
            b = carry & MASK

        # Handle negative results in python's 32-bit representation
        return a if a <= MAX_INT else ~(a ^ MASK)