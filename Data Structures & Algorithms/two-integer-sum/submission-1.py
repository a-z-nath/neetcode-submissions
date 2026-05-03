class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            if mp[target - nums[i]] > 0:
                return [mp[target - nums[i]] -1, i]
            mp[nums[i]] = i+1

        return [-1, -1]