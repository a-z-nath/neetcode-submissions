class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        candidate = []
        def backtrack(open: int, close: int):
            if len(candidate) == 2*n:
                res.append("".join(candidate))
                return
            if open < n:
                candidate.append("(")
                backtrack(open + 1, close)
                candidate.pop()
            if close < open:
                candidate.append(")")
                backtrack(open, close + 1)
                candidate.pop()
            
            return
        backtrack(0, 0)
        return res
        