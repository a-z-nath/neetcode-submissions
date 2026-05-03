class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(0, len(nums)):
            freq[nums[i]] += 1
        
        count = [[] for _ in range((len(nums) + 1))]
        for key, val in freq.items():
            count[val].append(key)
        
        ans = []
        for i in range(len(count) - 1, 0, -1):
            for j in count[i]:
                if len(ans) < k:
                    ans.append(j)

        return ans