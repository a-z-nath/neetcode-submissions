class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL <= maxR:
                trapped = maxL - height[l]
                res += max(trapped, 0)
                l += 1
                maxL = max(maxL, height[l])
            else:
                trapped = maxR - height[r]
                res += max(trapped, 0)
                r -= 1
                maxR = max(maxR, height[r])
                
        return res