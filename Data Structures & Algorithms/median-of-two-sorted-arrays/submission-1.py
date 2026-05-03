class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        l1, l2 = len(A), len(B)
        total = l1 + l2
        half = total // 2
        l, r = 0, l1 - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2 # 0 based 1 from A another from B
            Aleft = A[i] if i >= 0 else float("-inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Aright = A[i+1] if (i + 1) < l1 else float("inf")
            Bright = B[j+1] if (j + 1) < l2 else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        return -1