class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start, curSum, candidate):
            # found solution
            if target == curSum:
                res.append(candidate[:])
                return
            # handle invalid and outof range solutions
            if start >= len(candidates) or curSum > target:
                return
            # iterate all possible candidate
            for i in range(start, len(candidates)):
                if candidates[i] + curSum > target:
                    return
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                candidate.append(candidates[i])
                backtrack(i+1, curSum + candidates[i], candidate)
                candidate.pop()
            return
        backtrack(0, 0, [])
        return res