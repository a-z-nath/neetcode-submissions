class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        x = 1
        for i in range(31):
            if x & n > 0:
                count += 1
            x = x * 2
        return count