class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        monost = []
        for i, t in enumerate(temperatures):
            while monost and temperatures[monost[-1]] < t:
                idx = monost.pop()
                res[idx] = i - idx
            monost.append(i)
        return res