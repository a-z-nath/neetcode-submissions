class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def makeTargetSum(i: int, cursum: int):
            if i == len(nums):
                return int(target == cursum)
            if (i, cursum) in dp:
                return dp[(i, cursum)]
            add = makeTargetSum(i+1, cursum + nums[i])
            sub = makeTargetSum(i+1, cursum - nums[i])
            dp[(i, cursum)] = add + sub
            return dp[(i, cursum)]
        return makeTargetSum(0, 0)