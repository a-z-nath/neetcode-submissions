class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) -1
        res = nums[0]
        while low <= high:
            # already sorted low .. high
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break 

            mid = (low + high) // 2
            res = min(res, nums[mid])
            # left subtree
            if nums[mid] < nums[low]:
                high = mid
            else:
                low = mid + 1
        return res