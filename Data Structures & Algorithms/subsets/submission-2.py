class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, subset):
            res.append(subset[:]) # since for all its valid solution
            
            for i in range(start, len(nums)): # traverse all valid candidate
                subset.append(nums[i])  # place partial candidate
                backtrack(i+1, subset)  # explore further for given candidate
                subset.pop()            # backtrack
            return
        backtrack(0, [])
        return res