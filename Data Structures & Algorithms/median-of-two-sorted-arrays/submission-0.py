class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find mid elements.
        # n/2 + 1 , n/2 for even-> avg(n/2+1, n/2) -> 1 based
        # n/2 for odd.
        # parallel pointer.
        l1, l2 = len(nums1), len(nums2)
        mid = (l1 + l2) // 2
        median1 = median2 = 0
        p1, p2 = 0, 0
        for _ in range(mid + 1):
            median2 = median1
            if p1 < l1 and p2 < l2:
                if nums1[p1] <= nums2[p2]:
                    median1 = nums1[p1]
                    p1 +=1
                else:
                    median1 = nums2[p2]
                    p2 += 1
            elif p1 < l1:
                median1 = nums1[p1]
                p1 += 1
            else:
                median1 = nums2[p2]
                p2 += 1
        
        if (l1 + l2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2