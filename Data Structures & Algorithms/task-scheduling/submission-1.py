class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        mxfreq, k = max(count.values()), 0
        for f in count.values():
            if f == mxfreq:
                k += 1
        
        return max(len(tasks), (mxfreq-1) * (n+1) + k)