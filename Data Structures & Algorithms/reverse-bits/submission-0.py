class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(31):
            x = n & 1
            ans = ans | x
            n //= 2
            ans <<= 1
        ans |= n & 1
        return ans