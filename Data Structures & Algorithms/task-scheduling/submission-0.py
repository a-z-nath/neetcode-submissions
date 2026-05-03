class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for cnt in count.values():
            heapq.heappush(maxHeap, -1 * cnt)
        q = deque() # pairs of [-cnt, idleTime]

        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                cnt, _ = q.popleft()
                heapq.heappush(maxHeap, cnt)
        return time