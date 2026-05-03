class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count0 = 0
        prod = 1
        for n in nums:
            if  n == 0:
                count0 += 1
                continue
            prod *= n
        
        ans = [0 for _ in nums]
        if count0 > 1:
            return ans
        if count0 == 1:
            for i in range(0, len(nums)):
                if  nums[i] == 0:
                    ans[i] = prod
            return ans
        for i in range(0, len(nums)):
            ans[i] = prod // nums[i]
        return ans
            