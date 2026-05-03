class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n < 2:
            return [-1, -1]
        l, r = 0, n - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if target == sum:
                return [l+1, r+1]
            if sum > target:
                r -=1
            else:
                l += 1
        return [-1, -1]