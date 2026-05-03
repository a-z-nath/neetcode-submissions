class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while h - l > 1:
            mid = (l + h) // 2
            # left sorted arr
            # t > [mid] right
            # else t >= [l] -> left else right
            m = nums[mid]
            if nums[l] <= m:
                if target > m or target < nums[l]:
                    l = mid
                else:
                    h = mid

            # right sorted arr
            # t <= [mid] -> left
            # else t <= [h] -> right else left
            else:
                if target <= m or target > nums[h]:
                    h = mid
                else:
                    l = mid


            
        if nums[l] == target:
            return l
        elif nums[h] == target:
            return h
        else:
            return -1