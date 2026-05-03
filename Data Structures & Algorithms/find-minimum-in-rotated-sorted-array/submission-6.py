class Solution:
    def findMin(self, nums: List[int]) -> int:
        # mn = [0], mid < mn -> left, mid > mn -> right
        res = nums[0]
        l, h = 0, len(nums) - 1
        # sorted only
        if res < nums[h]:
            return res
        # sorted with rotation [1, len)
        while l < h:
            mid = (l + h) // 2
            if nums[mid] < res:
                h = mid
            else:
                l = mid + 1
        return nums[l]