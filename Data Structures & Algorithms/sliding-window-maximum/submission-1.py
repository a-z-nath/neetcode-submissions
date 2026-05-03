class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # calculate current max for win, update while drifting through the arr
        mx, secMx = [float("-inf"), -1], [float("-inf"), -1]
        res = []
        for i in range(k):
            if nums[i] >= mx[0]:
                mx = [nums[i], i]
                secMx = [float("-inf"), -1]
            elif nums[i] >=secMx[0] and i > mx[1]:
                secMx = [nums[i], i]
        res.append(mx[0])
        for i in range(1, len(nums) - k + 1):
            if nums[i+k - 1] >= mx[0]:
                mx = [nums[i+k - 1], i+k-1]
                secMx = [float("-inf"), -1]
            if nums[i+k - 1] >=secMx[0] and i+k-1 > mx[1]:
                secMx = [nums[i+k-1], i+k-1]
            if mx[1] < i:
                mx = secMx
                j = mx[1] + 1
                secMx = [float("-inf"), -1]
                while j < mx[1] + k and j < len(nums):
                    if nums[j] >= secMx[0]:
                        secMx = [nums[j], j]
                    j += 1
            res.append(mx[0])
        return res