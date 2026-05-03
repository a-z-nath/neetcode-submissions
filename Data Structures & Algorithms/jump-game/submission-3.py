class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # sum of idx, val >= len - 1 -> true
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0