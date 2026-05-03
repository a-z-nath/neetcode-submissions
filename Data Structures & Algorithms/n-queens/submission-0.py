class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        candidate = []
        col = set()
        def valid(i, j) -> bool:
            for row in range(len(candidate)):
                for col, c in enumerate(candidate[row]):
                    if c == "Q" and (j == col or abs(i-row) == abs(j-col)):
                        return False
            return True


        def backtrack(i: int):
            if i == n:
                res.append(["".join(rows) for rows in candidate])
                return
            row = ["."]*n
            for k in range(n):
                if valid(i, k):
                    row[k] = "Q"
                    # col.add(k)
                    candidate.append(row[:])
                    backtrack(i+1)
                    row[k] = "."
                    # col.remove(k)
                    candidate.pop()
            return
        backtrack(0)
        return res