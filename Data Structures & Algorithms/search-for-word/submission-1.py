class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        wsz = len(word)
        path = set()
        def backtrack(i, j, wi) -> bool:
            if wi == wsz :
                return True
            if -1>=i or i>=m :
                return False
            if -1>=j or j>=n :
                return False
            if (i,j) in path:
                return False
            f1 = f2 = f3 = f4 = False
            if board[i][j] == word[wi]:
                path.add((i,j))
                f1 = backtrack(i, j-1, wi+1)
                if f1:
                    path.remove((i,j))
                    return True
                f2 = backtrack(i, j+1, wi+1)
                if f2:
                    path.remove((i,j))
                    return True
                f3 = backtrack(i-1, j, wi+1)
                if f3:
                    path.remove((i,j))
                    return True
                f4 = backtrack(i+1, j, wi+1)
                if f4:
                    path.remove((i,j))
                    return True
                path.remove((i,j))
            return f1 or f2 or f3 or f4
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    print(path)
                    return True
        
        print(path)
        return False
            