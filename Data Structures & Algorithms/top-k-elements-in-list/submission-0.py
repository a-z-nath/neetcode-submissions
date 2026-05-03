class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(0, len(nums)):
            freq[nums[i]] += 1
        pairs = [(k, v) for k, v in freq.items()]
        pairs.sort(key = lambda x: x[1], reverse = True)
        
        ans = []
        for i in range(0, k):
            ans.append(pairs[i][0])
        
        return ans