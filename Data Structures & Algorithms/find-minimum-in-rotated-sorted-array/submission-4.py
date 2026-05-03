class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) -1
        if nums[low] < nums[high]:
            return nums[low]
        
        while high - low > 1:
            mid = (low + high) // 2
            print(low, mid, high)
            if nums[mid] > nums[low]:
                low = mid
            else:
                high = mid
        return min(nums[low], nums[high])