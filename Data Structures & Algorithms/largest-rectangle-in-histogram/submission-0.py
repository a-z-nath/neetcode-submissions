class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # indices
        mxArea = 0
        popidx, n = -1, len(heights)
        for i in range(len(heights)):
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                mxArea = max(mxArea, (i - idx) * height)
                popidx = idx
            popidx = i if popidx == -1 else popidx
            stack.append((popidx, heights[i]))
            popidx = -1
        for i in range(len(stack)-1, -1, -1):
            idx, height = stack[i]
            mxArea = max(mxArea, (n-idx) * height)
        return mxArea
