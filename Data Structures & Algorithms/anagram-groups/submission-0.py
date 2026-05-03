class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(0, len(strs)):
            count = [0] * 26
            for j in range(0, len(strs[i])):
                count[ord(strs[i][j]) - ord("a")] += 1
            key = ""
            for k in range(0, 26):
                key += str(ord('0') + count[k])
            res[key].append(strs[i])
        ans = []
        for key in res.keys():
            ans.append(res[key])
        
        return ans