class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dcmap = {2:"abc",
        3:"def", 4: "ghi", 5: "jkl", 6: "mno",
        7:"pqrs", 8:"tuv", 9: "wxyz"
        }
        res:List[str] = []
        n = len(digits)
        def backtrack(i, candidate):
            if i == n:
                if not candidate:
                    return
                res.append(candidate)
                return
            digit = int(digits[i])
            for ch in dcmap[digit]:
                backtrack(i+1, candidate+ch)
            return
        backtrack(0, "")
        return res