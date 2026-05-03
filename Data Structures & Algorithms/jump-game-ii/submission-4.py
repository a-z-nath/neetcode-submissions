class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left = right = 0
        while right < len(nums) -1 :
            furthest = 0
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])
            jumps += 1
            left = right + 1
            right = furthest
        return jumps