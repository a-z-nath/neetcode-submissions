class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i: int) -> bool:
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                print("reached")
                return True
            
            end = min(len(nums)-1, i + nums[i])
            for k in range(end, i, -1):
                if dfs(k):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)