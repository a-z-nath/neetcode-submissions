class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        visited = set()
        cur, i = float("-inf"), 0
        while i < len(hand):
            if i in visited or cur == hand[i]:
                i += 1
                continue
            if cur == float("-inf"):
                cur = hand[i]
                visited.add(i)
            elif cur + 1 == hand[i]:
                cur += 1
                visited.add(i)
            else:
                return False
            if len(visited) % groupSize == 0:
                i = 0
                cur = float("-inf")
            i += 1
        return True if len(visited) % groupSize == 0 else False