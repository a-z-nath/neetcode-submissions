class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            mid = (l + h) // 2
            # left sorted
            if nums[l]<= nums[mid]:
                if nums[l] > target or nums[mid] < target :
                    l = mid + 1
                else:
                    h = mid
            else:
                if target <= nums[mid] or target > nums[h]:
                    h = mid
                else:
                    l = mid + 1
        
        return l if nums[l] == target else -1