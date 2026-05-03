class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        prevEnd = float("-inf")
        cnt = 0
        for s, e in intervals:
            if s >= prevEnd:
                prevEnd = e
            else:
                cnt += 1
        return cnt