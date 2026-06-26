class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(0, len(nums)):
            rem = target - nums[i]
            if rem in mp:
                return [mp[rem], i]
            if nums[i] not in mp:
                mp[nums[i]] = i
        return [-1, -1]