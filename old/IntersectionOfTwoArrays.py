class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp=set()
        unique=set()
        res=list()
        for item in nums1:
            tmp.add(item)
        
        for item in nums2:
            if item in tmp and item not in unique:
                res.append(item)
                unique.add(item)
        return res
