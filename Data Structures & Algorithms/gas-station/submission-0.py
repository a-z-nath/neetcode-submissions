class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, n = 0, len(gas)
        tank = 0
        while start < len(gas):
            for i in range(len(gas)):
                tank += (gas[(i+start) % n] - cost[(i+start) % n])
                if tank < 0:
                    tank = 0
                    start += 1
                    print(start)
                    break
                if i == n-1:
                    return start
        return -1
