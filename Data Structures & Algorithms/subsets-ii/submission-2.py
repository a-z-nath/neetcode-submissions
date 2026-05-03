class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(start, candidate):
            res.append(candidate[:])
            # iterate all possible state
            for i in range(start, len(nums)):
                # take or skip all duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                candidate.append(nums[i])
                backtrack(i+1, candidate)
                candidate.pop()
            return
        backtrack(0, [])
        return res