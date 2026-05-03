class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for x in nums:
            sum += x
        n = len(nums)
        predsum = (n * (n+1)) // 2
        return predsum - sum