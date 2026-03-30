class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res.sort()
        n = len(res)
        mid = len(res) // 2
        if n % 2 == 0:
            return float((res[mid] + res[mid - 1])/2)
        else:
            return float(res[mid])