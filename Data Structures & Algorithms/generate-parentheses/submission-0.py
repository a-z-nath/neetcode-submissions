class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(left: int, closes: int, candidate: str):
            if left == n and closes == n:
                # sol
                res.append(candidate[:])
                return

            if left < n:
                backtrack(left+1, closes, candidate+"(")
            if closes < left:
                backtrack(left, closes+1, candidate+")")
            return
        backtrack(0,0, "")
        return res