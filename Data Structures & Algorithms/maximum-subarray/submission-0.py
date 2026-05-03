class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxSum, localSum = float("-inf"), 0
        for n in nums:
            localSum += n
            mxSum = max(mxSum, localSum)
            if localSum < 0:
                localSum = 0
        return mxSum