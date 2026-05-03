class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = float("-inf")
        for n in nums:
            tmp = curMin * n
            curMin = min(tmp, curMax * n, n)
            curMax = max(tmp, curMax * n, n)
            res = max(res, curMin, curMax)
            if curMin == curMax == 0:
                curMin, curMax = 1, 1
        return res