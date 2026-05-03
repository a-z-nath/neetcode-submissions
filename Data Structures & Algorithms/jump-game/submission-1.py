class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def dfs(i: int) -> bool:
            if i == len(nums) - 1:
                print("reached")
                return True
            if i >= len(nums):
                return False
            flag = False
            for k in range(i + nums[i], i, -1):
                flag = dfs(k)
                if flag:
                    break
            return flag
        
        return dfs(0)