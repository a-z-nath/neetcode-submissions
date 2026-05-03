class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while h - l > 1:
            mid = (l + h) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid
        
        if nums[l] == target:
            return l
        elif nums[h] == target:
            return h
        else:
            return -1