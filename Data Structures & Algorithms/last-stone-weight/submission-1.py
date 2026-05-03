class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x != y:
                heapq.heappush_max(stones, abs(x - y))
        if not stones:
            return 0
        return stones[0]