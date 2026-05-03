class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def backtrack(i: int, j: int, candidate: List[str]):
            if i == j and j == n:
                res.append(candidate[:])
                return
            if i < j and j == n:
                return
            def palindrome(i:int, j:int):
                p, q = i, j
                while p < q:
                    if s[p] != s[q]:
                        return False
                    p += 1
                    q -= 1
                return True
            if palindrome(i, j):
                candidate.append(s[i:j+1])
                backtrack(j+1, j+1, candidate)
                candidate.pop()
            backtrack(i, j+1, candidate)
            return
        
        backtrack(0, 0, [])
        return res
            
            
