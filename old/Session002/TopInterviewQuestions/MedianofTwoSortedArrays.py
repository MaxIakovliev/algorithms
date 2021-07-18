class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total=sorted(nums1+nums2)
        size=len(total)
        if size %2==0:
            return (total[size //2 -1]+total[size//2])/2.0
        return total[size//2]
        