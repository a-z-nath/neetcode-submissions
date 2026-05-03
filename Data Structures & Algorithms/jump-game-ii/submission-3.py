class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]
            if i >= len(nums) -1:
                return 0
            if nums[i] == 0:
                return float("inf")
            end = min(len(nums) - 1, i + nums[i])
            res = float("inf")
            for k in range(end, i, -1):
                res = min(res, 1 + dfs(k))
            memo[i] = res
            return res
        return dfs(0)