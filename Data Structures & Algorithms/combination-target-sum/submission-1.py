class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(start, curSum, candidate):
            # solution candidate
            if curSum == target:
                print(start, candidate)
                res.append(candidate[:])
                return
            if start >= len(nums) or curSum > target:
                return
            
            for i in range(start, len(nums)):
                total = curSum + nums[i]
                if total <= target:
                    candidate.append(nums[i])
                    backtrack(i, total, candidate)
                    candidate.pop()
                else:
                    return
            return
        backtrack(0, 0, [])
        return res